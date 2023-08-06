# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forbidden_comments']

package_data = \
{'': ['*']}

install_requires = \
['nbconvert>=6.1.0,<7.0.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['forbidden_comments = forbidden_comments.__main__:app']}

setup_kwargs = {
    'name': 'forbidden-comments',
    'version': '0.1.0',
    'description': 'A tool to inspect your Notebooks for useless comments',
    'long_description': None,
    'author': 'Antonio Feregrino',
    'author_email': 'antonio.feregrino@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
