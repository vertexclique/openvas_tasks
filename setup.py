#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """
Information and history receptor for OpenVAS tasks.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
    'license': 'GPLv3',
    'url': 'http://vertexclique.github.io/openvas_tasks',
    'download_url': 'https://github.com/vertexclique/openvas_tasks/zipball/master',
    'install_requires': requires,
    'zip_safe': False,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Affero General Public License v3',
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