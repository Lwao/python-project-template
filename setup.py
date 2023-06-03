from setuptools import setup, find_packages

VERSION = '0.0.0'
DESCRIPTION = ''
LONG_DESCRIPTION = ''

setup(
    name='app',
    version=VERSION,
    url='',
    author='John Smith',
    author_email='john@email.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={'console_scripts': ['cli=cli.cli:start']},
    keywords=['python'],
    classifiers= [ # https://pypi.org/classifiers/
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operationg System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
)