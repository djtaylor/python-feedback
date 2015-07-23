#!/usr/bin/python
import feedback
from setuptools import setup, find_packages

# Module version / long description
version = feedback.__version__
long_desc = open('README.md').read()

# Run the setup
setup(
    name='feedback',
    version=version,
    description='Feedback and user input manager',
    long_description=long_desc,
    author='David Taylor',
    author_email='djtaylor13@gmail.com',
    url='http://github.com/djtaylor/python-feedback',
    license='GPLv3',
    packages=find_packages(),
)