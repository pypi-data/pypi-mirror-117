.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/cedadev/xarray_pickler/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

xarray-pickler could always use more documentation, whether as part of the
official xarray-pickler docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/cedadev/xarray_pickler/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.


Get Started!
------------

Ready to contribute? Here's how to set up `xarray_pickler` for local development.

1. Fork the `xarray_pickler` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/xarray_pickler.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv xarray_pickler
    $ cd xarray_pickler/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5.  When you are done making changes, check that your changes pass flake8 and the
    tests, including testing other Python versions with tox::

    $ flake8 clisops tests
    $ black --target-version py36 clisops tests
    $ pytest tests

    To get flake8, black, and tox, just pip install them into your virtualenv.
    Alternatively, you can use `pre-commit` to perform these checks at the git commit stage::

    $ pip install pre-commit
    $ pre-commit install
    $ pre-commit run --all-files

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6, 3.7 and 3.8. Check
   https://travis-ci.com/cedadev/xarray_pickler/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests/test_xarray_pickler.py::test_get_pickle_path


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ git tag <tagname>
$ git push origin <tagname>

Where the tag name is the raw version e.g. 0.1.0
GitHub Actions will then deploy to PyPI if tests pass.
