# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['readmemd2txt']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['readmemd2txt = readmemd2txt.readmemd2txt:main']}

setup_kwargs = {
    'name': 'readmemd2txt',
    'version': '0.0.4',
    'description': 'Quick and dirty converter: README.md > pure text',
    'long_description': None,
    'author': 'suizokukan',
    'author_email': 'suizokukan@orange.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
