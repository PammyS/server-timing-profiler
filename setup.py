import os
try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup, Command

BASE_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(BASE_DIR, 'README.md')
DESCRIPTION = open(README_PATH).read()

setup(
    name='server-timing-profiler',
    version='0.0.2',
    description='HTTP Server-Timing for Python Flask',
    long_description=DESCRIPTION,
    license='Apache License 2.0',
    author='Perminder Singh',
    author_email='svicky9797@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask==0.10.1'
    ],
    keywords='HTTP Server-Timing for Python Flask',
    url='https://github.com/PammyS/server-timing-profiler',
    namespace_packages=[],
    platforms='Linux, POSIX',
    entry_points={
        'console_scripts': [
            '',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)