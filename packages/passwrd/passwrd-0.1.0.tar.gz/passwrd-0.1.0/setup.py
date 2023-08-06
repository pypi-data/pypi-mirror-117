# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['passwrd']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'passwrd',
    'version': '0.1.0',
    'description': 'Python tool to generate secure mnemonic passwords.',
    'long_description': None,
    'author': 'samedamci',
    'author_email': 'samedamci@disroot.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/samedamci/passwrd',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
