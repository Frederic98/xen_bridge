import enum
import keyword
import re
import textwrap
import urllib.parse
from typing import Union, List, Dict
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

INDENTATION = ' '*4

RE_SET = re.compile(r'^(.*) set$')
RE_DICT = re.compile(r'^\((.+?) → (.*)\) map$')     # Assuming there is no dict as key values
RE_XEN = re.compile(r'^(.*) ref$')
RE_ENUM = re.compile(r'^enum (.*)$')
RE_RECORD = re.compile(r'^(.*) record$')
RE_OPTION = re.compile(r'^(.*) option')

RE_GETSET = re.compile(r'^(?:get|set)_(.+)$')


class AccessType(enum.Enum):
    READONLY = 0b01
    WRITEONLY = 0b10
    READWRITE = READONLY | WRITEONLY
    def code(self):
        return f'XenProperty.{self.name}'
class Argument:
    def __init__(self, name: str, type: str):
        self.name = sanitize_name(name)
        self.type = parse_type(type)
    def __str__(self):
        if self.type is None: return self.name
        else: return f'{self.name}: {self.type}'
class XenMethod:
    def __init__(self, name: str, args: List[Argument], type: str, description: str=None):
        self.name = sanitize_name(name)
        self.arguments = args
        self.type = parse_type(type)
        self.description = description
    def code(self):
        argstr = ['self'] + [str(arg) for arg in self.arguments]
        returnstr = f' -> {self.type}' if self.type is not None else ''
        if self.description:
            body = f'"""{textwrap.fill(self.description, width=80)}"""'
        else:
            body = '...'
        body = textwrap.indent(body, INDENTATION)
        return f"@XenMethod\ndef {self.name}({', '.join(argstr)}){returnstr}:\n{body}"
class XenProperty:
    def __init__(self, name: str, type: str, access: str, description: str=None):
        self.name = sanitize_name(name)
        self.type = parse_type(type)
        self.description = description
        if re.search('RO', access):
            self.access = AccessType.READONLY
        elif re.search('WO', access):
            self.access = AccessType.WRITEONLY
        elif re.search('RW', access):
            self.access = AccessType.READWRITE
        else:
            raise ValueError(f'Unknown access type for {self.name} ({access})')
    def code(self):
        annotation = f': {self.type}' if self.type is not None else ''
        description = f", {repr(unidecode(self.description))}" if self.description is not None else ''
        return f'{self.name}{annotation} = XenProperty({self.access.code()}{description})'
class XenEnum:
    def __init__(self, name: str, values: List[str] = None):
        name = ''.join([word.title() for word in name.split('_')])
        self.name = sanitize_name(name)
        self.values = values
    def __str__(self): return self.name
    def code(self):
        fields = ''.join([f"{sanitize_name(v.upper())} = '{v}'\n" for v in self.values])
        return f'class {self.name}(XenEnum):\n' + textwrap.indent(fields, INDENTATION)
class XenRef:
    def __init__(self, name: str, globalscope: bool = True):
        self.name = sanitize_name(CamelCase(name))
        self.scope = 'xenbridge.' if globalscope else ''
    def __str__(self): return f"'{self.scope}{self.name}'"
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, XenRef):
            return self.name == other.name
        return False
class XenClass:
    def __init__(self, name: str, enums: Dict[str, XenEnum],
                                  properties: Dict[str, XenProperty],
                                  methods: Dict[str, XenMethod]):
        self.name = sanitize_name(name)
        self.class_name = sanitize_name(CamelCase(name))
        self.enums: Dict[str, XenEnum] = enums
        self.properties: Dict[str, XenProperty] = properties
        self.staticmethods: Dict[str, XenMethod] = {}
        self.boundmethods: Dict[str, XenMethod] = {}
        for name, method in methods.items():
            if method.arguments[0].type != 'Session':
                print(f'Skipping method {self.name}.{name} - no session argument!')
                continue
            if RE_GETSET.match(method.name):
                if RE_GETSET.match(method.name).group(1) in self.properties:
                    # getter / setter method for property - automatically generated by XenProperty
                    continue
            if len(method.arguments) > 1 and method.arguments[1].type == self.class_name:
                method.arguments = method.arguments[2:]
                self.boundmethods[name] = method
            else:
                method.arguments = method.arguments[1:]
                self.staticmethods[name] = method

    def code(self):
        code = ''
        if len(self.enums):
            for name, member in self.enums.items():
                code += member.code()
            code += '\n'

        code += f'class {self.class_name}(XenObject):\n'
        code += f"    xenpath='{self.name}'\n\n"

        for group in (self.properties, self.boundmethods):
            if len(group):
                for name, member in group.items():
                    code += textwrap.indent(member.code(), INDENTATION)
                    code += '\n'
                    # for line in member.code().split('\n'):
                    #     code += '    ' + line + '\n'
                code += '\n'


        code += f'\nclass {self.class_name}Endpoint(XenEndpoint):\n'
        code += f"    xenpath='{self.name}'\n"
        if self.staticmethods:
            for name, member in self.staticmethods.items():
                code += textwrap.indent(member.code(), INDENTATION)
                code += '\n'
                # for line in member.code().split('\n'):
                #     code += '    ' + line + '\n'
        else:
            code += '    ...\n'
        return code

    def all(self):
        return f'{self.class_name}, {self.class_name}Endpoint'


def parse_page(url: str):
    resp = requests.get(url)
    resp.raise_for_status()
    doc = BeautifulSoup(resp.text, features="html.parser")
    content = doc.find(id='content')
    members: Dict[str, List[Union['XenMethod', 'XenProperty', 'XenEnum']]] = {'methods': [],
                                                                     'staticmethods': []}
    enums: Dict[str, XenEnum] = {}
    properties: Dict[str, XenProperty] = {}
    methods: Dict[str, XenMethod] = {}
    class_name = re.match('Class: (.*)', content.find(class_='title').text.strip()).group(1)
    doc_section = None

    for elem in content.find_all(recursive=False):
        if elem.name.lower() == 'h3':
            doc_section = elem.find(text=True, recursive=False).strip().lower()
            if doc_section not in members:
                members[doc_section] = []
        elif doc_section is not None\
                and elem.get('class') is not None\
                and any(tag in elem.get('class') for tag in ('field', 'field2')):
            # Parse Enums
            if doc_section == 'enums':
                name = elem.find(class_='field-name').text
                argtable = elem.find(class_='field-table')
                values_section = False
                values = []
                for row in argtable.find_all('tr'):
                    field_head = row.find(class_='field-head').text.lower().strip()
                    if 'value' in field_head:
                        values_section = True
                    elif field_head != '':
                        break
                    if values_section:
                        valueelem = row.find_all('td')[1]
                        values.append(valueelem.text)
                enums[name] = XenEnum(name, values)
            # Parse Properties
            if doc_section == 'fields':
                name = elem.find(class_='field-name').text
                type = elem.find(class_='inline-type').text
                access = elem.find(class_='inline-qualifier').text
                description = elem.find(class_='field-description').text.strip()
                properties[name] = XenProperty(name, type, access, description)
            # Parse Methods
            elif doc_section == 'messages':
                name = elem.find(class_='field-name').text
                type = elem.find(class_='inline-type').text
                description = elem.find(class_='field-description').text.strip()
                args = []
                argtable = elem.find(class_='field-table')
                params = False
                for row in argtable.find_all('tr'):
                    field_head = row.find(class_='field-head').text.lower().strip()
                    if 'parameter' in field_head:
                        params = True
                    elif field_head != '':
                        break
                    if params:
                        paramelem = row.find_all('td')[1]
                        param_type, param_name = paramelem.text.rsplit(' ', 1)
                        args.append(Argument(param_name, param_type))
                methods[name] = XenMethod(name, args, type, description)
    return XenClass(class_name, enums, properties, methods)


def parse_type(type_str: str):
    type_str = type_str.strip()
    if type_str == 'string': return 'str'
    if type_str == 'int': return 'int'
    if type_str == 'float': return 'float'
    if type_str == 'bool': return 'bool'
    if type_str == 'datetime': return 'datetime.datetime'
    if type_str == 'void': return 'None'
    if RE_SET.match(type_str):
        type_str = RE_SET.match(type_str).group(1)
        return f'List[{parse_type(type_str)}]'
    if RE_DICT.match(type_str):
        key, value = RE_DICT.match(type_str).groups()
        return f'Dict[{parse_type(key)}, {parse_type(value)}]'
    if RE_RECORD.match(type_str):
        return 'Dict[str, Any]'
    if RE_OPTION.match(type_str):
        type_str = RE_OPTION.match(type_str).group(1)
        return f'Optional[{parse_type(type_str)}]'
    if RE_XEN.match(type_str):
        type_str = RE_XEN.match(type_str).group(1)
        return XenRef(type_str)
    if RE_ENUM.match(type_str):
        type_str = RE_ENUM.match(type_str).group(1)
        return XenEnum(type_str)
    print(f'!!! Unknown type "{type_str}"')
    return None
    # return f'!UNKNOWN({type_str})'

def sanitize_name(name: str):
    name = name.replace('-', '_')
    if keyword.iskeyword(name):
        return name + '_'
    return name

def CamelCase(name: str):
    words = name.split('_')
    return ''.join(word[0].upper() + word[1:] for word in words)

main_url = 'https://xapi-project.github.io/xen-api/index.html'
resp = requests.get(main_url)
resp.raise_for_status()
main_page = BeautifulSoup(resp.text, features='html.parser')
navbar = main_page.find(id='sidebar')
endpoints = {}
with open('xenbridge/__init__.py', 'w') as init_f:
    for url in navbar.find_all('a', recursive=False):
        print(f'--- {url.text} ---')
        page_url = urllib.parse.urljoin(main_url, url['href'])
        cls = parse_page(page_url)
        with open(f'xenbridge/{cls.name.lower()}.py', 'w') as f:
            f.write(f'#Automatically generated from {page_url}\n')
            f.write('import xenbridge\n')
            f.write('from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum\n')
            f.write('from typing import List, Dict, Any, Optional\n')
            f.write('import datetime\n')
            f.write('\n\n')
            f.write(cls.code())
        init_f.write(f'from .{cls.name.lower()} import {cls.all()}\n')
        endpoints[cls.class_name] = f'{cls.class_name}Endpoint'
    init_f.write('from .xenobject import XenObject, XenEndpoint\n')
    init_f.write('from .xenconnection import XenConnectionBase\n')
    # init_f.write('from .xenobject import XenObject, XenEndpoint, XenConnectionBase\n')
    init_f.write('\nclass XenConnection(XenConnectionBase):\n')
    for name, type in endpoints.items():
        init_f.write(f'    {name}: {type}\n')
