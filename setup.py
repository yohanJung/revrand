#!/usr/bin/env python
""" Setup utility for the pyalacarte package. """

from setuptools import setup

setup(
    name='pyalacarte',
    version='0.1',
    description='Implementation of the A la Carte approximation of Gaussian'
                'processes, amongst other things.',
    author='Daniel Steinberg',
    author_email='daniel.steinberg@nicta.com.au',
    url='',
    packages=['pyalacarte'],
    install_requires=[
        'scipy >= 0.14.1',
        'numpy >= 1.8.2',
        'wget >= 2.2',
        # NLopt >= 2.4.2
    ],
    license = "Apache Software License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ]
)
