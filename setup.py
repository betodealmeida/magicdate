RELEASE = True

from setuptools import setup, find_packages
import sys, os

classifiers = """\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

version = '0.1.3'

setup(name='magicdate',
      version=version,
      description="Convert fuzzy date to a datetime object.",
      long_description="""\
Convert from fuzzy dates like "yesterday", "2 weeks and 1 day ago", "next wed", "Jan 4", etc., to a datetime object.

This is useful for processing command line arguments::

    >>> from optparse import OptionParser
    >>> import magicdate
    >>> parser = OptionParser(option_class=magicdate.MagicDateOption)
    >>> parser.add_option('-s', '--start', dest='start', type='magicdate', default=None)
    >>> parser.add_option('-e', '--end', dest='end', type='magicdate', default='today')
    
Now you can pass options like "today", "1996-01-01", etc., to your program.

Inspired by Simon Willison's ``dateparse.js``.

""",
      classifiers=filter(None, classifiers.split("\n")),
      keywords='datetime time',
      author='Roberto De Almeida',
      author_email='rob@pydap.org',
      #url='http://dealmeida.net/projects/magicdate',
      download_url = "http://cheeseshop.python.org/packages/source/m/magicdate/magicdate-%s.tar.gz" % version,
      license='MIT',
      py_modules=['magicdate'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
      
