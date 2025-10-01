# EntityIdentity Install Test

[![Tests](https://img.shields.io/badge/tests-22%20passed-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.8+-blue)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

This repository provides comprehensive tests and examples for the [entityidentity](https://github.com/microprediction/entityidentity) package.

**Status**: ✅ All 22 tests passing

## Quick Start

### Option 1: Install as Package (Recommended)

```bash
# Install the package
pip install -e .

# Run tests via command
entityidentity-test

# Run examples via command
entityidentity-examples
```

### Option 2: Direct Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests with pytest
pytest -v

# Run specific test files
pytest tests/test_import.py -v              # Basic functionality
pytest tests/test_data_resolution.py -v     # Comprehensive data tests

# Run examples
python tests/examples.py
# Or: python -m tests.examples
```

### Option 3: Quick Shell Script

```bash
./run_tests.sh
```

## What is EntityIdentity?

Entity resolution and identity matching for companies. Fast, in-memory company name resolution using fuzzy matching and smart normalization. No server required.

### Key Features

- **Fast in-memory lookups**: <100ms for most queries
- **Multiple data sources**: GLEIF LEI, Wikidata, stock exchanges
- **Smart normalization**: Handles legal suffixes, punctuation, unicode
- **Fuzzy matching**: RapidFuzz scoring with intelligent blocking
- **No dependencies**: Works out of the box

## Included Tests

### Basic Tests (test_import.py)
Simple tests covering the main API functions.

### Comprehensive Tests (test_data_resolution.py)
Rigorous tests that verify the package data and functionality:
- ✅ **Data Availability**: Database loads with proper structure and multiple countries
- ✅ **Entity Resolution**: Tests matching functionality with various company names
- ✅ **Name Normalization**: Properly handles legal suffixes, punctuation, and case
- ✅ **Country Filtering**: Filters by country and has international data
- ✅ **Search Quality**: Name search returns relevant results
- ✅ **Matching Behavior**: Tests matching function behavior and error handling
- ✅ **Data Sources**: Includes LEI data and multiple source verification

**Note**: Tests are designed to be resilient and work with the actual API behavior.

### Examples (examples.py)
Practical usage demonstrations for all major features.

### Documentation
- [INSTALL.md](INSTALL.md) - Complete installation guide
- [TEST_COVERAGE.md](TEST_COVERAGE.md) - Detailed test coverage information
- [TEST_RESULTS.md](TEST_RESULTS.md) - Latest test results (all pass! ✅)
- [BUGS_FOUND.md](BUGS_FOUND.md) - Known issues in the package

## Learn More

For full documentation, see the [main repository](https://github.com/microprediction/entityidentity).

## License

MIT

