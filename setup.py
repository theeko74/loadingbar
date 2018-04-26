"""
A setuptools based setup module.
"""

from setuptools import setup, find_packages
import loading

setup(
    name='loading',
    version=loading.__version__,
    description="Library to display a loading bar in a terminal.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Sylvain Carlioz',
    author_email='sylvain.carlioz@gmail.com',
    keywords='loading, loading bar, terminal',
    url='https://github.com/theeko74/loading',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],

    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    #install_requires=[],
)
