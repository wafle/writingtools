#!/usr/bin/env python
from setuptools import setup

setup(
    name='writingtools',
    version=0.1,
    description="Collection of tools for writing papers",
    author='Janos Maginecz',
    author_email='wafleeee@gmail.com',
    url='https://github.com/wafle/writing-tools',
    license='MIT',
    packages=[],
    install_requires=['requests_futures', 'beautifulsoup4'],
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': [
        'gcompare = writingtools.gcompare:main',
        'synonym = writingtools.synonym:main'
    ]}
)
