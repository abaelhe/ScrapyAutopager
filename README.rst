=========
Autopager
=========

.. image:: https://img.shields.io/pypi/v/autopager.svg
   :target: https://pypi.python.org/pypi/autopager
   :alt: PyPI Version

.. image:: https://img.shields.io/travis/TeamHG-Memex/autopager/master.svg
   :target: http://travis-ci.org/TeamHG-Memex/autopager
   :alt: Build Status

.. image:: http://codecov.io/github/TeamHG-Memex/autopager/coverage.svg?branch=master
   :target: http://codecov.io/github/TeamHG-Memex/autopager?branch=master
   :alt: Code Coverage


Autopager is a Python package which detects and classifies pagination links.

License is MIT.

How It Works
============

Autopager uses machine learning to detect paginators. It classifies
``<a>`` HTML elements into 5 classes:

* PREV - previous page link
* PAGE - a link to a specific page
* NEXT - next page link
* LAST - 'got to last page' link which is not just a number
* FIRST - 'got to first page' link which is not just '1' number
* OTHER - not a pagination link

To do that it uses features like link text, URL parts and right/left contexts.
CRF is used for learning.

Web page is represented as a sequence of ``<a>`` elements.

Training Data
=============

Data is stored at autopager/data. Raw HTML source code
is in autopager/data/html folder. Annotations are in autopager/data/data.csv
file; elements are stored as CSS selectors.

To add a new page to training data save it to an html file
and add a row to the data.csv file. It is helpful
to use http://selectorgadget.com/ extension to get CSS selectors.
