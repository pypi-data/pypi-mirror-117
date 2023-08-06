# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['stackx']
setup_kwargs = {
    'name': 'stackx',
    'version': '1.0.0',
    'description': 'Stack(*elements)',
    'long_description': None,
    'author': 'semenchuk Community',
    'author_email': 'hootuk@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
