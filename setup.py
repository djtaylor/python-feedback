#!/usr/bin/python
from sys import path
from setuptools import setup, find_packages

# Add the local path
path.append('usr/local/lib/python2.7/dist-packages')

# Import the module version
from feedback import __version__

# Module version / long description
version   = __version__
long_desc = open('DESCRIPTION.rst').read()

# Run the setup
setup(
    name             = 'feedback',
    version          = version,
    description      = 'Feedback and user input manager',
    long_description = long_desc,
    author           = 'David Taylor',
    author_email     = 'djtaylor13@gmail.com',
    url              = 'http://github.com/djtaylor/python-feedback',
    license          = 'GPLv3',
    install_requires = ['colorama>=0.2.5', 'termcolor>=1.1.0'],
    packages         = find_packages(),
    keywords         = 'feedback terminal shell ui output input',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
    ]
)