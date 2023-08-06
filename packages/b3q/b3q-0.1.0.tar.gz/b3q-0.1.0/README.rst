===
b3q
===

Boto3 utility library that supports parameter-driven and predicate-driven retrieval of collections of AWS resources.

|pypi| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/b3q.svg
   :target: https://badge.fury.io/py/b3q
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/nthparty/b3q.svg?branch=main
   :target: https://travis-ci.com/nthparty/b3q

.. |coveralls| image:: https://coveralls.io/repos/github/nthparty/blooms/badge.svg?branch=main
   :target: https://coveralls.io/github/nthparty/b3q?branch=main

Purpose
-------
This library makes it possible to use `Boto3 <https://boto3.readthedocs.io>`_ to retrieve a collection of AWS resources (selected according to supplied parameters, constraints, and/or predicates) within an AWS service.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install b3q

The library can be imported in the usual ways::

    import b3q
    from b3q import *

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configution details)::

    nosetests

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python b3q/b3q.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint b3q

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
