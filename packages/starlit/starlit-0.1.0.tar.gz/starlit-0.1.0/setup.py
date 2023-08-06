# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'starlit',
    'version': '0.1.0',
    'description': '🌠 Neural Architecture Definition Framework',
    'long_description': '# starlit\n🌠 Neural Architecture Definition Framework\n',
    'author': 'Hundgeburth Laurenz',
    'author_email': 'laurenzbeck@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
