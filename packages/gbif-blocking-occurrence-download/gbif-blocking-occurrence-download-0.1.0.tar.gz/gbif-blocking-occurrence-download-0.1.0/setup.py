# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['gbif_blocking_occurrences_download']
install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'gbif-blocking-occurrence-download',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Nicolas Noé',
    'author_email': 'nicolas.noe@inbo.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
