# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['begentle']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.18.0,<3.0.0']

setup_kwargs = {
    'name': 'begentle',
    'version': '0.1.0',
    'description': "A module for filtering text with profanity using Google's Perspective API.",
    'long_description': "begentle\n========\nbegentle is a package for detecting toxic language using \nthe Perspective API (more info at `PerspectiveAPI.com <https://perspectiveapi.com/>`_).\nGoogle already has a Python module for this, but I think it's \ntoo complex, so I created my own.\n\n",
    'author': 'Rahul Wavare',
    'author_email': 'rahulrakida@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
