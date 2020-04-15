================================
Behave 4 Command Line Interfaces
================================

.. image:: https://img.shields.io/pypi/v/behave4git.svg
    :target: https://pypi.python.org/pypi/behave4git

.. image:: https://github.com/opinionated-digital-center/behave4git/workflows/Test%20and%20make%20release/badge.svg
    :target: https://github.com/opinionated-digital-center/behave4git/pipelines
    :alt: Linux build

This project provides an extension (testing domain) of `Behave`_ to use Git and GitLab
(and GitHub in the near future)

* Free software license: MIT

Features
--------

* Create a clean working directory
* Create and delete environment variables
* Run commands and check success/failure, return code and output
* Create, delete and check existence of directories
* Create, delete, check existence and check content of files
* Check for current date and working directory paths in commands output and
  files content

How to use
----------

Import the steps you want to use by creating a python file (we name it by convention
``use_steplib_behave4git.py``) in your ``features/steps`` directory::

  # -- REGISTER-STEPS FROM STEP-LIBRARY:
  import behave4git.__all_steps__

Credits
-------

See ``LICENSE`` file for most code credits/copyrights.

This package was created with Cookiecutter_ and the
`opinionated-digital-center/cookiecutter-pypackage`_ project template.

.. _Behave: https://github.com/behave/behave
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _Black: https://black.readthedocs.io/en/stable/
.. _isort: https://timothycrosley.github.io/isort/
.. _Behave bdd tests: https://github.com/behave/behave/tree/v1.2.6/features
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`opinionated-digital-center/cookiecutter-pypackage`: https://github.com/opinionated-digital-center/cookiecutter-pypackage
