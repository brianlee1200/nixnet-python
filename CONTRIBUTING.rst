Contributing to nixnet
=======================

Contributions to **nixnet** are welcome from all!

**nixnet** is managed via `git <https://git-scm.com>`_, with the canonical
upstream repository hosted on `GitHub <http://developercertificate.org/>`_.

**nixnet** follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project,
push a branch with your changes to your project, and then submit a pull
request.

See `GitHub's official documentation <https://help.github.com/articles/using-pull-requests/>`_
for more details.

Getting Started
---------------

To contribute to this project, it is recommended that you follow these steps:

1. Fork the repository on GitHub.
2. Run the unit tests on your system (see Testing section). At this point,
   if any tests fail, do not begin development. Try to investigate these
   failures. If you're unable to do so, report an issue through our
   `GitHub issues page <http://github.com/ni/nixnet-python/issues>`_.
3. Write new tests that demonstrate your bug or feature. Ensure that these
   new tests fail.
4. Make your change.
5. Run all the unit tests again (which include the tests you just added),
   and confirm that they all pass.
6. Send a GitHub Pull Request to the main repository's master branch. GitHub
   Pull Requests are the expected method of code collaboration on this project.

.. _testing-section:

Testing
-------

In order to be able to run the **nixnet** unit tests, your setup should meet
the following minimum requirements:

  - Setup has a machine with NI-XNET or the NI-XNET Runtime installed.
  - Machine has a supported version of CPython or PyPy installed.
  - **TODO** Document required hardware and system setup.

To run the **nixnet** unit tests in a specific version of Python, run
the following command in the root of the distribution::

  $ <Python executable> setup.py test

To run the unit tests in all Python interpreters supported by **nixnet**,
run the following commands in the root of the distribution::

  $ pip install tox
  $ tox

This requires you to have all the Python interpreters supported by
**nixnet** installed on your machine.

Developer Certificate of Origin (DCO)
-------------------------------------

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

(taken from `developercertificate.org <http://developercertificate.org/>`_)

See `LICENSE <https://github.com/ni/nixnet-python/blob/master/LICENSE>`_
for details about how **nixnet** is licensed.
