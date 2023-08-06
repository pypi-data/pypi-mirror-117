# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['queueq']
setup_kwargs = {
    'name': 'queueq',
    'version': '1.1.0',
    'description': 'Queue(*elements)',
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
