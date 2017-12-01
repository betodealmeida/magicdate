from setuptools import setup
RELEASE = True

classifiers = """
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

version = '0.2.1'

setup(
    name='magicdate',
    version=version,
    description="Convert fuzzy date to a datetime object.",
    long_description="""
Convert from fuzzy dates like "yesterday", "2 weeks and 1 day ago", "next wed",
"Jan 4", etc., to a datetime object.

This is useful for processing command line arguments::

    >>> from optparse import OptionParser
    >>> import magicdate
    >>> parser = OptionParser(option_class=magicdate.MagicDateOption)
    >>> parser.add_option(
    ...     '-s', '--start', dest='start', type='magicdate', default=None)
    >>> parser.add_option(
    ...     '-e', '--end', dest='end', type='magicdate', default='today')

Now you can pass options like "today", "1996-01-01", etc., to your program.

Inspired by Simon Willison's ``dateparse.js``.

""",
    classifiers=[c for c in classifiers.split("\n") if c],
    keywords='datetime time',
    author='Beto Dealmeida',
    author_email='roberto@dealmeida.net',
    url='https://github.com/betodealmeida/magicdate',
    license='MIT',
    py_modules=['magicdate'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    entry_points="""
        [console_scripts]
        magicdate = magicdate:main
    """,
)
