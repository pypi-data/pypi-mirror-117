============
gocept.month
============

.. image:: https://img.shields.io/pypi/v/gocept.month.svg
    :target: https://pypi.org/project/gocept.month/

.. image:: https://img.shields.io/pypi/pyversions/gocept.month.svg
    :target: https://pypi.org/project/gocept.month/

.. image:: https://github.com/gocept/gocept.month/workflows/tests/badge.svg
    :target: https://github.com/gocept/gocept.month/actions?query=workflow%3Atests

.. image:: https://coveralls.io/repos/github/gocept/gocept.month/badge.svg?branch=master
    :target: https://coveralls.io/github/gocept/gocept.month?branch=master

.. image:: https://results.pre-commit.ci/badge/github/gocept/gocept.month/main.svg
   :target: https://results.pre-commit.ci/latest/github/gocept/gocept.month/main
   :alt: pre-commit.ci status


A datatype which stores a year and a month.

This package provides the data type ``Month`` (typical usage:
``Month(4, 2003)``), which supports conversion to and from strings, as well as
a zope.schema field and widgets for both zope.formlib and z3c.form.

To use the month field, ``<include package="gocept.month"/>`` and declare a
schema like this:

    >>> import gocept.month
    >>> import zope.interface
    >>> import zope.schema
    >>> class IContract(zope.interface.Interface):
    ...     title = zope.schema.TextLine(title=u"Contract title")
    ...     start = gocept.month.MonthField(title=u"Starting date")
    ...     end = gocept.month.MonthField(title=u"Ending date")

To use the form widgets, you need to require the ``form`` setuptools extra
(i.e. ``gocept.month[form]``), and ``<include
package="gocept.month.browser"/>`` in your ZCML.
