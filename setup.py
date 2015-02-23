try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Learning Python Exercises',
    'author': 'Nathan Danielsen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'nathan.danielsen@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['learn'],
    'scripts': ['bin/script.py'],
    'name': 'learn'
}

setup(**config)