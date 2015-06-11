DJTP Watcher
============

.. contents::
  :local:
  :depth: 2

Watcher serves for ``djtp`` repository maintainance with:

- code coverage
- pep8 compatible code
- python 2 and python 3 compatibility

DJTP submodule
--------------
djtp checks provide `tox <https://testrun.org/tox/latest/>`_ over
djtp git repository (powered with git submodule).

.. code-block:: bash

  user@localhost djtp_watcher $ git submodule init djtp

  Submodule 'djtp' (https://github.com/tarvitz/djtp.git) registered for path 'djtp'

  user@localhost djtp_watcher $ git submodule update djtp
  Cloning into 'djtp'...
  remote: Counting objects: 839, done.
  remote: Compressing objects: 100% (89/89), done.
  remote: Total 839 (delta 33), reused 0 (delta 0), pack-reused 747
  Receiving objects: 100% (839/839), 1.20 MiB | 434.00 KiB/s, done.
  Resolving deltas: 100% (425/425), done.
  Checking connectivity... done.
  Submodule path 'djtp': checked out '77ad9d3b9298017e3f26dc0f8407ea1dd76ae6c1'

Testing
-------
Whole tests powered by tox:

.. code-block:: bash

  user@localhost djtp_watcher $ tox

  <cut info>
  _______________________ summary _______________________
  py27: commands succeeded
  py33: commands succeeded
  py34: commands succeeded
  flake8: commands succeeded
  congratulations :)
