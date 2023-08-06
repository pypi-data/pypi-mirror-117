# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testp0131']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'testp0131',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'qiujingyu',
    'author_email': 'qiujingyu@momenta.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
