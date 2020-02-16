.. image:: https://img.shields.io/pypi/v/csv2tabulate
        :alt: PyPI
        :target: https://pypi.org/project/csv2tabulate/

.. image:: https://img.shields.io/pypi/pyversions/csv2tabulate
        :alt: PyPI - Python Version
        :target: https://pypi.org/project/csv2tabulate/

.. image:: https://img.shields.io/travis/frafra/csv2tabulate
        :alt: Travis (.org)
        :target: https://travis-ci.com/frafra/csv2tabulate/

.. image:: https://img.shields.io/codecov/c/github/frafra/csv2tabulate
        :alt: Codecov
        :target: https://codecov.io/gh/frafra/csv2tabulate

How to install
==============

.. code:: bash

  pip install csv2tabulate

Examples
========

Convert from CSV to reStructuredText
------------------------------------

.. code:: bash

  csv2tabulate --output table.rst --format rst table.csv

Convert from recfile to Markdown
--------------------------------

.. code:: bash

  rec2csv table.rec | csv2tabulate --output table.md
