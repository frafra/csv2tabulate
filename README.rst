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
