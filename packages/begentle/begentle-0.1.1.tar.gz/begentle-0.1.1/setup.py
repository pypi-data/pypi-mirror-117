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
    'version': '0.1.1',
    'description': "A module for filtering text with profanity using Google's Perspective API.",
    'long_description': "========\nbegentle\n========\nbegentle is a package for detecting toxic language using \nthe Perspective API (more info at `PerspectiveAPI.com <https://perspectiveapi.com/>`_).\nGoogle already has a Python module for this, but I think it's \ntoo complex, so I created my own.\n\nGetting Started\n---------------\nFirst you will need a Google Cloud project API key with\nthe Perspective API enabled. \n\nFollow these two tutorials:\n| `Tutorial 1: Getting Started <https://developers.perspectiveapi.com/s/docs-get-started>`_\n| `Tutorial 2: Enable the API <https://developers.perspectiveapi.com/s/docs-enable-the-api>`_\n\nOnce you have your API key install the package::\n\n    pip install begentle\n\nand use it like so::\n    \n    from begentle import CommentAnalyzer\n    analyzer = CommentAnalyzer('YOUR_API_KEY')\n    comment = 'You suck! I hate you, never come back.'\n    print(analyzer.analyze(comment))\n\nYou should see something like 0.9543847.\nThis is a value between 0 and 1 representing toxicity.\nGenerally toxic phrases return a value above 0.9.\nAnd that's it!",
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
