# -*- coding: utf-8 -*-
"""
This module contains the tool of ecreall.trashcan
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.4'

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
#    + '\n' +
#    'Detailed Documentation\n'
#    '**********************\n'
#    + '\n' +
#    read('ecreall', 'trashcan', 'README.txt')
#    + '\n' +
#    'Contributors\n'
#    '============\n'
#    + '\n' +
#    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '========\n'
    )

tests_require=['zope.testing']

setup(name='ecreall.trashcan',
      version=version,
      description="Trashcan for Plone. By Ecreall.",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Vincent Fretin and Michael Launay',
      author_email='development@ecreall.com',
      url='http://pypi.python.org/pypi/ecreall.trashcan',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ecreall', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'collective.monkeypatcher',
                        'Plone >= 3.3',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'ecreall.trashcan.tests.test_docs.test_suite',
      entry_points="""
      """,
      )
