# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ardkit',
 'ardkit.api',
 'ardkit.core',
 'ardkit.core.db',
 'ardkit.core.event',
 'ardkit.core.log',
 'ardkit.core.net',
 'ardkit.core.system']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ardkit',
    'version': '0.1.0',
    'description': 'Ardkit, the open source cloud',
    'long_description': None,
    'author': 'Ardustri',
    'author_email': 'ardkit@ardustri.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
