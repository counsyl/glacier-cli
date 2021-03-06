from setuptools import setup

setup(name='glacier-cli',
      version='0.1',
      py_modules=['glacier', 'gpg'],
      license='BSD',
      description='Command-line interface to Amazon Glacier',
      install_requires=[
        'boto',
        'iso8601',
        'sqlalchemy',
        'python-gnupg'
      ]
)
