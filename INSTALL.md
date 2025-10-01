# Installation Guide

## Package Installation

This test suite can be installed as a Python package.

### Standard Installation

```bash
# Clone the repository
git clone https://github.com/microprediction/entityidentity-installtest.git
cd entityidentity-installtest

# Install the package
pip install -e .
```

### What Gets Installed

- ✅ The `entityidentity` package (main dependency)
- ✅ `pytest` for running tests
- ✅ Command-line tools:
  - `entityidentity-test` - Run the test suite
  - `entityidentity-examples` - Run usage examples

### Development Installation

For development with additional tools:

```bash
# Install with development dependencies
pip install -e ".[dev]"
```

This includes:
- `pytest-cov` - Code coverage
- `black` - Code formatting
- `flake8` - Linting

## Running Tests

### Using the Package Commands

After installation, you can run tests from anywhere:

```bash
# Run all tests
entityidentity-test

# Run with specific pytest options
entityidentity-test --verbose
entityidentity-test -k "test_normalize"
entityidentity-test --markers

# Run examples
entityidentity-examples
```

### Using pytest Directly

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tests --cov-report=html

# Run specific test file
pytest tests/test_import.py

# Run specific test class
pytest tests/test_data_resolution.py::TestDataAvailability

# Run specific test function
pytest tests/test_import.py::test_normalize_name

# Run tests with specific marker
pytest -m data
pytest -m resolution
```

### Using the Shell Script

```bash
./run_tests.sh
```

### Direct Python Execution

```bash
# Run test file directly
python tests/test_import.py
python tests/test_data_resolution.py

# Run examples
python tests/examples.py
python -m tests.examples
```

## Package Structure

```
entityidentity-installtest/
├── setup.py                    # Package setup (setuptools)
├── pyproject.toml             # Modern package config
├── MANIFEST.in                # Files to include in distribution
├── requirements.txt           # Runtime dependencies
├── requirements-dev.txt       # Development dependencies
├── pytest.ini                 # Pytest configuration
├── tests/
│   ├── __init__.py           # Package marker
│   ├── conftest.py           # Pytest fixtures and config
│   ├── run.py                # CLI test runner
│   ├── test_import.py        # Basic tests
│   ├── test_data_resolution.py # Comprehensive tests
│   └── examples.py           # Usage examples
└── ...
```

## Verifying Installation

After installation, verify everything works:

```bash
# Check package is installed
pip show entityidentity-installtest

# Check commands are available
which entityidentity-test
which entityidentity-examples

# Run quick test
entityidentity-test -v

# Run examples
entityidentity-examples
```

## Uninstalling

```bash
pip uninstall entityidentity-installtest
```

## Building Distribution

To create a distribution package:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates:
# dist/entityidentity_installtest-1.0.0-py3-none-any.whl
# dist/entityidentity-installtest-1.0.0.tar.gz
```

## Publishing (for maintainers)

```bash
# Test PyPI
python -m twine upload --repository testpypi dist/*

# Production PyPI
python -m twine upload dist/*
```

Then users can install with:
```bash
pip install entityidentity-installtest
```

## Troubleshooting

### Command not found

If `entityidentity-test` is not found:
```bash
# Make sure the package is installed
pip install -e .

# Check your PATH includes pip bin directory
pip show entityidentity-installtest
```

### Import errors

If tests can't import modules:
```bash
# Reinstall in editable mode
pip install -e .

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Permission errors on run_tests.sh

```bash
chmod +x run_tests.sh
```

