try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'gecko',
    'author': 'Adam Miritis',
    'url': 'https://github.com/Foxh0und/gecko',
    'download_url': 'https://github.com/Foxh0und/gecko',
    'author_email': 'amiritis@wolfmail.co',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gecko'],
    'scripts': [],
    'name': 'gecko'
}

setup(**config)