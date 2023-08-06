import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iotkaran",
    version="0.0.1",
    author="reza behjani",
    author_email="iotkaran2020@gmail.com",
    description="library for connect to server iotkaran ",
    long_description='''# Project description
this library for connect to server iotkaran and send data to dashboard 

Addres Dashboard :https://dashboard.iotkaran.ir 
> Automatic Installation
```
pip3 install iotkaran
```
www.iotkaran.ir

[GitHub](http://github.com/iotkaran)

> Example

> Automatic Installation
```
>>> from iotkaran import IotK
>>> iotkaran.connect to server(""server.iotkaran.ir",2323)
```''' ,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/iotkaran",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/iotkaran/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)