# To build, publish, and test published package:
# This file stays in the parent dir of the thing I'm building the whl for, because
# find_packages() is going to look in subdirectories.  If you run this from the
# pybrick directory, it'll build a package with nothing in it.
# C:\OPP\blurry>python setup.py bdist_wheel
# twine upload dist/*
# Set up a test environment:
# C:\temp>virtualenv --python=C:\Python35\python3.5.exe take5
# C:\temp>.\take5\Scripts\activate
# (take5) C:\temp>pip install pybrick
# (take5) C:\temp>python
# ActivePython 3.5.4.3504 (ActiveState Software Inc.) based on
# Python 3.5.4 (default, Dec 15 2017, 14:24:56) [MSC v.1900 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from pybrick import pybrick

import setuptools
setuptools.setup(
      name='pybrick',
      description='A python/yellowbrick interface utility',
      long_description='A python/yellowbrick interface utility',
      version='0.1.3',
      url='https://github.com/iamlevis/blurry/pybrick',
      author='Chris Levis',
      author_email='chris.levis@gmail.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=setuptools.find_packages(),
      install_requires=[
          'pandas'
         ,'pyodbc'
      ],
      entry_points={
          'console_scripts': [
              'encrypt=pybrick.main:run'
          ]
      }
)
