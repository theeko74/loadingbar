"""
A setuptools based setup module.
"""

from setuptools import setup, find_packages
import loading

setup(
    name='loading',
    version=loading.__version__,
    description="Loading module to display loading bar indicator in a terminal window",
    long_description=open('README.md').read(),
    license='MIT',
    author='Sylvain Carlioz',
    author_email='sylvain.carlioz@gmail.com',
    keywords='loading bar',
    url='https://github.com/theeko74/loading',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.5',
    ],

    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    #install_requires=[],
)
