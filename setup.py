try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r', encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='validate_nigerian_phone',
    version='1.0.0',
    description='Python Class to validate a Nigerian phone number as well as attempt to deduce the network',
    long_description=long_description,
    author='Zacchaeus Bolaji',
    author_email='djunehor@gmail.com',
    url='https://github.com/djunehor/validate_nigerian_phone',
    packages=['validate_nigerian_phone'],

)