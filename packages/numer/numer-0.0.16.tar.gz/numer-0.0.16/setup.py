from setuptools import setup, find_packages

VERSION = '0.0.16'
DESCRIPTION = 'Example implementation of gmp and C math.h functions'
LONG_DESCRIPTION = 'Simple arithmetic functions from C and gmp'

# Setting up
setup(
    name="numer",
    version=VERSION,
    author="Ar-Ed",
    author_email="<rased27273333@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=['numer'],
    package_data={
        'numer': ['gmp.dylib',  'lib.dylib', 'gmp.dll', 'lib.dll']
    },
    install_requires=[],
    keywords=['python', 'math', 'gmp', 'cmath'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)