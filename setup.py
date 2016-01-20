#!/usr/bin/env python3
from sys import version_info
from setuptools import setup
from uflash import get_version


with open('README.rst') as f:
    readme = f.read()
with open('CHANGES.rst') as f:
    changes = f.read()


install_requires = [
    'pytest',
    'pep8',
    'pyflakes',
    'coverage',
    'sphinx',
    'pytest-cov',
]

if version_info.major == 2:
    install_requires.append([
        'mock',
        'future',
    ])

setup(
    name='uflash',
    version=get_version(),
    description='A module and utility to flash Python onto the BBC micro:bit.',
    long_description=readme + '\n\n' + changes,
    author='Nicholas H.Tollervey',
    author_email='ntoll@ntoll.org',
    url='https://github.com/ntoll/uflash',
    py_modules=['uflash', ],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Software Development :: Embedded Systems',
    ],
    entry_points={
        'console_scripts': ['uflash=uflash:main'],
    },
    install_requires=install_requires,
)
