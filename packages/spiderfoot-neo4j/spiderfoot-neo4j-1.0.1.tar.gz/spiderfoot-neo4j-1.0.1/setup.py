# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spiderfoot_neo4j']

package_data = \
{'': ['*']}

install_requires = \
['py2neo>=2021.1.5,<2022.0.0', 'tld>=0.12.6,<0.13.0']

entry_points = \
{'console_scripts': ['sfgraph = spiderfoot_neo4j.sfgraph:go']}

setup_kwargs = {
    'name': 'spiderfoot-neo4j',
    'version': '1.0.1',
    'description': 'Import, visualize, and analyze SpiderFoot scans in Neo4j, a graph database',
    'long_description': None,
    'author': 'TheTechromancer',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/blacklanternsecurity/spiderfoot-neo4j',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
