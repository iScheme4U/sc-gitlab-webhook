.. image:: https://badge.fury.io/py/sc-gitlab-webhook.svg
    :target: https://badge.fury.io/py/sc-gitlab-webhook
.. image:: https://img.shields.io/pypi/pyversions/sc-gitlab-webhook
    :alt: PyPI - Python Version

A simple Gitlab WebHook
========================================

This project provides a Gitlab web hook to receive Gitlab events and process these events.


Installation
------------

It is possible to install the tool with `pip`::

    pip install sc-gitlab-webhook

Configuration
-------------

You can copy `default.yml <tests/sample_config/default.yml>`_ to `~/.sc-gitlab-webhook/production.yml`
to initialize the production configuration.

See `default.yml <tests/sample_config/default.yml>`_ for more information.

Dependencies
------------

* sc-config 0.0.2
* flask 1.1.2
* rocketmq-client-python 2.0.0

Changes
-------

Version 0.0.1
    * Initial version

License
-------

The script is released under the MIT License.  The MIT License is registered
with and approved by the Open Source Initiative [1]_.

.. [1] https://opensource.org/licenses/MIT
