# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['doublelinkedstruct']
setup_kwargs = {
    'name': 'doublelinkedstruct',
    'version': '1.0.0',
    'description': 'List(*elements)',
    'long_description': None,
    'author': 'semechuk Community',
    'author_email': 'hootuk@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
