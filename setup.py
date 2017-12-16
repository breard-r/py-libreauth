from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='libreauth',
    version='0.1.0.dev3',
    description='Python bindings to the LibreAuth library.',
    long_description=long_description,
    url='https://github.com/breard-r/py-libreauth',
    author='Rodolphe Bréard',
    author_email='rodolphe@breard.tf',
    license='CeCILL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Security',
    ],
    keywords='authentication password oath hotp totp',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='~=3.3',
    data_files=[
        ('license', ['LICENSE-EN.txt', 'LICENSE-FR.txt']),
    ],
)
