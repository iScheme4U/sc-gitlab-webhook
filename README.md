 [![PyPI Version](https://badge.fury.io/py/sc-gitlab-webhook.svg)](https://badge.fury.io/py/sc-gitlab-webhook)
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sc-gitlab-webhook)](https://img.shields.io/pypi/pyversions/sc-gitlab-webhook)

# A simple Gitlab WebHook

This project provides a Gitlab web hook to receive Gitlab events and process these events.

## Installation

It is possible to install the tool with pip:

```
pip install sc-gitlab-webhook
```

## Configuration

You can copy [default.yml](tests/sample_config/default.yml) to `~/.sc-gitlab-webhook/production.yml`
to initialize the production configuration.

- See [default.yml](tests/sample_config/default.yml) for more information.

## Dependencies

- config42 0.4.4
- flask 1.1.2

## Changes

- Version 0.0.1

  - Initial version

## License

The script is released under the [MIT License](https://opensource.org/licenses/MIT). 
The MIT License is registered with and approved by the [Open Source Initiative](https://opensource.org/).
