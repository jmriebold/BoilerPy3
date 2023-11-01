import os

from setuptools import setup

from boilerpy3 import __version__

_BASE_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.join(_BASE_DIR, 'README.md')) as readme_file:
    long_description = readme_file.read()

setup(
        name='boilerpy3',
        version=__version__,
        python_requires='>=3.6',
        author='John Riebold',
        author_email='jmriebold@gmail.com',
        license='Apache 2.0',
        description='Python port of Boilerpipe, for HTML boilerplate removal and text extraction',
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords=[
            'boilerpipe',
            'boilerpy',
            'html text extraction',
            'text extraction',
            'full text extraction'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Topic :: Utilities',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10'
        ],
        url='https://github.com/jmriebold/BoilerPy3',
        packages=[
            'boilerpy3'
        ]
)
