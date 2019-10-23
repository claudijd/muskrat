try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': '',
    'url': '',
    'download_url': '',
    'author_email': 'jclaudius@mozilla.com',
    'version': "0.0.1",
    'install_requires': [],
    'packages': ['muskrat'],
    'scripts': [],
    'data_files': [],
    'name': 'muskrat'
}

setup(**config)
