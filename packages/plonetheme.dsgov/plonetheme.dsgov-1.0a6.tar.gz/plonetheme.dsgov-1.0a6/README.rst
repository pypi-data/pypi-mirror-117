.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.


================
plonetheme.dsgov
================

A theme for PLome 5 using the Design System of the Brazilian Federal Government (DSGovBR)

Features
--------

- GovBr layout for your website with the Content Management System - Plone 5.
- Support for custom tiles with mosaic

Documentation
-------------

- The theme is inspired by Barcelometa and uses Plone 5 without format as its base theme.


Installation
------------

In Production

This component is still under development,
for now the installation can be done by cloning this directory
inside the src folder of your website and configuring the buildout to
fetch the package from there. Or you can upload your site using the
buildout available here.

At the end of the [buildout] session in your buildout.cfg
Insert the following code like::


   [buildout]
   ...
   extensions = mr.developer
   # Tell mr.developer to ask before updating a checkout.
   always-checkout = true
   show-picked-versions = true
   sources = sources

   ...

   eggs =
       Plone
       Pillow
       # development tools
       plonetheme.dsgov
   ...

Run buildout::

    $ buildout

In Development

Set up a virtual environment using python 3.8

Then run the command::

    $ pip install -r requirements.txt

Run buildout::

    $ buildout

Start Plone in foreground::

    $ instance fg

Contribute
----------

- Issue Tracker: https://github.com/collective/plonetheme.dsgov/issues
- Source Code: https://github.com/collective/plonetheme.dsgov


Support
-------

If you have any suggestions for improvement, please contribute to: https://github.com/collective/plonetheme.dsgov/issues


License
-------

The project is licensed under the GPLv2.

