#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """
Information and history receptor for OpenVAS tasks.

Copyright (c) 2014-2015 Mahmut Bulut

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__all__ = ["metadata", "main"]

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Text describing the module.
description = 'Information and history receptor for OpenVAS tasks'

requires = ['peewee']

try:
    readme = os.path.join(os.getcwd(), 'README.md')
    long_description = open(readme, 'rU').read()
except IOError:
    long_description = description

# Set the parameters for the setup script.
metadata = {

    # Setup instructions.
    'provides': ['openvas_tasks'],
    'packages': ['openvas_tasks'],

    # Metadata.
    'name': 'openvas_tasks',
    'version': '1.0',
    'description': description,
    'long_description': long_description,
    'author': 'Mahmut Bulut (vertexclique)',
    'author_email': 'mahmut' + '@' + 'mahmutbulut.com',
    'license': 'MIT',
    'url': 'http://vertexclique.github.io/openvas_tasks',
    'download_url': 'https://github.com/vertexclique/openvas_tasks/zipball/master',
    'install_requires': requires,
    'zip_safe': False,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
}


# Execute the setup script.
def main():
    setup(**metadata)


if __name__ == '__main__':
    main()
