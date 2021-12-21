from setuptools import find_packages, setup
import os
from io import open

def read_file(path, encoding='utf-8'):
    with open(os.path.join(os.path.dirname(__file__), path),
              encoding=encoding) as fp:
        return fp.read()

setup(
    name='pyfract',
    packages=find_packages(),
    version='1.1',
    description='Fractions implementation for Python',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Błażej Wrzosok',
    license='MIT',
    install_requires=[],
    url='https://github.com/wblazej/pyfract',
    keywords=['math', 'fractions', 'fract', 'numerator', 'denominator'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)