# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sinaspider']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'sinaspider',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Bao Hengtao',
    'author_email': 'baohengtao@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
