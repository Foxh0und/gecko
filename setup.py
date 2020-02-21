try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Adam Miritis',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'amiritis@wolfmail.co',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gecko'],
    'scripts': [],
    'name': 'gecko'
}

setup(**config)