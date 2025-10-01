# EntityIdentity Install Test

This repository provides minimal tests and examples for the [entityidentity](https://github.com/microprediction/entityidentity) package.

## Quick Start

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Run tests:**

```bash
# Quick test runner (recommended)
./run_tests.sh

# Or run with pytest directly
pytest -v

# Or run specific test suites
pytest tests/test_import.py -v              # Basic functionality
pytest tests/test_data_resolution.py -v     # Comprehensive data tests
```

3. **Run examples:**

```bash
python tests/examples.py
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

For detailed test coverage information, see [TEST_COVERAGE.md](TEST_COVERAGE.md).

## Learn More

For full documentation, see the [main repository](https://github.com/microprediction/entityidentity).

## License

MIT

