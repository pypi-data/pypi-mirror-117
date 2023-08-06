# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['goodboy']

package_data = \
{'': ['*'],
 'goodboy': ['locale/*', 'locale/en/LC_MESSAGES/*', 'locale/ru/LC_MESSAGES/*']}

setup_kwargs = {
    'name': 'goodboy',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Maxim Andryunin',
    'author_email': 'maxim.andryunin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
