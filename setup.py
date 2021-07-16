from setuptools import setup
from setuptools import find_packages


setup_options = {
    'name': 'mobijeSQL',
    'version': '0.1.2-alpha',
    'description': '',
    'author': 'HwDhyeon',
    'author_email': 'youfsk@mobigen.com',
    'url': 'https://github.com/mobigen/IRIS-E2E',
    'python_requires': '>=3.9',
    'packages': find_packages(),
    'install_requires': [
        'sqlalchemy>=1.4.11',
        'pydantic>=1.8.1',
        'pymysql>=1.0.2',
        'python-dotenv>=0.17.1'
    ],
    'zip_safe': False,
}

setup(**setup_options)
