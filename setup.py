import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xen-bridge",
    version="0.1",
    author="Frederic98",
    description="an object-oriented Xen API for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Frederic98/xen_bridge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where='.'),
    python_requires=">=3.8",
)
