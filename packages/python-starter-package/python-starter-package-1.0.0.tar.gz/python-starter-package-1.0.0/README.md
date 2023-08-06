# python-starter

[![GitHub Actions][github-actions-badge]](https://github.com/paulsabyasachi/python-starter/actions/)
[![Code style: black][black-badge]](https://github.com/psf/black)
[![Imports: isort][isort-badge]](https://pycqa.github.io/isort/)

[github-actions-badge]: https://github.com/paulsabyasachi/python-starter/workflows/python/badge.svg
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[isort-badge]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336

Example Python project that demonstrates how to create a tested Python package using the latest
Python testing and linting tooling. The project contains a `div` package that provides a simple
implementation of division (`div.lib`)
and a command line interface (`div.cli`).

## Requirements

Python 3.6+.

> **Note**
>
> Because [Python 2.7 support ended January 1, 2020](https://pythonclock.org/), new projects 
> should consider supporting Python 3 only, which is simpler than trying to support both. As a 
> result, support for Python 2.7 in this example project has been dropped.

## Running CLI application

- `export PYTHONPATH="${PYTHONPATH}:<path_to_directory>/python-starter/src"`
- `python cli.py -a 5 -b 2`

## Dependencies

Dependencies are defined in:

- `requirements.txt`
- `dev-requirements.txt`

### Virtual Environments

It is best practice during development to create an
isolated [Python virtualenv wrapper](https://www.geeksforgeeks.org/using-mkvirtualenv-to-create-new-virtual-environment-python/) using the `mkvirtualenv`
command. This will keep dependant Python packages from interfering with other
Python projects on your system.

On *Nix:

```bash
$ mkvirtualenv -p python3.x venv
```

It is good practice to update core packaging tools (`pip`, `setuptools`,
and `wheel`) to the latest versions.

```bash
(venv) $ python -m pip install --upgrade pip setuptools wheel
```

### Installing Dependencies

To update dependencies:

```bash
(venv) $ pip install -r requirements.txt
(venv) $ pip install -r dev-requirements.txt
```

After upgrading dependencies, run the unit tests as described in the [Unit Testing](#unit-testing)
section to ensure that none of the updated packages caused incompatibilities in the current
project.

## Packaging

This project is designed as a Python package, meaning that it can be bundled up and redistributed
as a single compressed file.

Packaging is configured by:

- `pyproject.toml`
- `setup.py`
- `MANIFEST.in`

To package the project as both a 
[source distribution](https://docs.python.org/3/distutils/sourcedist.html) and
a [wheel](https://wheel.readthedocs.io/en/stable/):

```bash
(venv) $ python setup.py sdist bdist_wheel
```

This will generate `dist/div-1.0.0.tar.gz` and `dist/div-1.0.0-py3-none-any.whl`.

Read more about the [advantages of wheels](https://pythonwheels.com/) to understand why generating
wheel distributions are important.

### Upload Distributions to PyPI

Source and wheel redistributable packages can
be [uploaded to PyPI](https://packaging.python.org/tutorials/packaging-projects/) or installed
directly from the filesystem using `pip`.

To upload to PyPI:

```bash
(venv) $ python -m pip install twine
(venv) $ twine upload dist/*
```

## Testing

Automated testing is performed using [tox](https://tox.readthedocs.io/en/latest/index.html). tox
will automatically create virtual environments based on `tox.ini` for unit testing, PEP8 style
guide checking, and documentation generation.

```bash
# Run all environments.
#   To only run a single environment, specify it like: -e lint
# command above.
(venv) $ tox
```

### Unit Testing

Unit testing is performed with [pytest](https://pytest.org/). pytest has become the defacto Python
unit testing framework. Some key advantages over the built
in [unittest](https://docs.python.org/3/library/unittest.html) module are:

1. Significantly less boilerplate needed for tests.
2. PEP8 compliant names (e.g. `pytest.raises()` instead of `self.assertRaises()`).
3. Vibrant ecosystem of plugins.

pytest will automatically discover and run tests by recursively searching for folders and `.py`
files prefixed with `test` for any functions prefixed by `test`.

The `tests` folder is created as a Python package (i.e. there is an `__init__.py` file within it)
because this helps `pytest` uniquely namespace the test files. Without this, two test files cannot
be named the same, even if they are in different sub-directories.

Code coverage is provided by the [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) plugin.

When running a unit test tox environment (e.g. `tox -e py36`), an HTML report is generated in
the `htmlcov` folder showing each source file and which lines were executed during unit testing.
Open `htmlcov/index.html` in a web browser to view the report. Code coverage reports help identify
areas of the project that are currently not tested.

Code coverage is configured in `pyproject.toml`.

To pass arguments to `pytest` through `tox`:

```bash
(venv) $ tox -e py36 -- -k invalid_divide
```

### Code Style Checking

[PEP8](https://www.python.org/dev/peps/pep-0008/) is the universally accepted style guide for
Python code. PEP8 code compliance is verified using [flake8](http://flake8.pycqa.org/). flake8 is
configured in the `[flake8]` section of `tox.ini`. Extra flake8 plugins are also included:

- `pep8-naming`: Ensure functions, classes, and variables are named with correct casing.

### Automated Code Formatting

Code is automatically formatted using [black](https://github.com/psf/black). Imports are
automatically sorted and grouped using [isort](https://github.com/PyCQA/isort/).

These tools are configured by:

- `pyproject.toml`

To automatically format code, run:

```bash
(venv) $ tox -e fmt
```

To verify code has been formatted, such as in a CI job:

```bash
(venv) $ tox -e fmt-check
```

### Generated API Documentation

#### Generate a New Sphinx Project

To generate the Sphinx project shown in this project:

```bash
(venv) $ mkdir -p docs/api
(venv) $ cd docs/api
(venv) $ sphinx-quickstart --no-makefile --no-batchfile --extensions sphinx.ext.napoleon
# When prompted, select all defaults.
```

Modify `conf.py` appropriately:

```python
# Add the project's Python package to the path so that autodoc can find it.
import os
import sys
sys.path.insert(0, os.path.abspath("../../src"))
```

You might also need to add `apidoc/modules.rst` in `index.rst` file (See line number 13). This has already been done for this project but might be helpful if you start a project of your own. 

API Documentation for the `div` Python project modules is automatically
generated using a [Sphinx](http://sphinx-doc.org/) tox environment. Sphinx is a documentation
generation tool that is the defacto tool for Python API documentation. Sphinx uses
the [RST](https://www.sphinx-doc.org/en/latest/usage/restructuredtext/basics.html) markup language.

This project uses
the [napoleon](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) plugin for
Sphinx, which renders Google-style docstrings. Google-style docstrings provide a good mix of
easy-to-read docstrings in code as well as nicely-rendered output.

```python
"""Divides first input with the second input.

Args:
    a: Numerator
    b: Denominator

Raises:
    InvalidDivideError: If denominator is 0

Returns:
    Computed division.
"""
```

The Sphinx project is configured in `docs/api/conf.py`.

This project uses the [furo](https://pradyunsg.me/furo/) Sphinx theme for its elegant, simple to
use, dark theme.

Build the docs using the `docs-api` tox environment (e.g. `tox` or `tox -e docs-api`). Once built,
open `docs/api/_build/index.html` in a web browser.

To configure Sphinx to automatically rebuild when it detects changes, run `tox -e docs-api-serve`
and open <http://127.0.0.1:8000> in a browser.
