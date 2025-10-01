# EntityIdentity Package Tests

Minimal tests and examples for the [entityidentity](https://github.com/microprediction/entityidentity) package.

## Installation

First, install the package:

```bash
pip install entityidentity
```

## Running Tests

Run all tests:

```bash
pytest -v
```

Or run specific test files:

```bash
# Basic import tests
pytest tests/test_import.py -v

# Data and resolution tests (comprehensive)
pytest tests/test_data_resolution.py -v
```

Run from test files directly:

```bash
python tests/test_import.py
python tests/test_data_resolution.py
```

## Running Examples

See the package in action:

```bash
python tests/examples.py
```

## What's Tested

### test_import.py - Basic Functionality
Minimal tests covering the main API:
- **`normalize_name()`** - Company name normalization
- **`match_company()`** - Simple company matching
- **`resolve_company()`** - Full resolution with details
- **`list_companies()`** - Listing and filtering companies
- **`load_companies()`** - Loading the company database

### test_data_resolution.py - Comprehensive Tests
Rigorous tests that verify data quality and resolution:
- **Data Availability** - Database loads with proper structure
- **Entity Resolution** - Tests matching functionality with known companies
- **Normalization** - Removes legal suffixes and handles punctuation
- **Country Filtering** - Multi-country data and filtering works
- **Search Functionality** - Name search and combined filters
- **Matching Quality** - Tests matching behavior and error handling
- **Data Sources** - LEI data and multiple source verification

**Note**: Tests are resilient to package bugs and work with the actual API (`list_companies`, not `load_companies`).

## Learn More

See the [main repository](https://github.com/microprediction/entityidentity) for full documentation.
