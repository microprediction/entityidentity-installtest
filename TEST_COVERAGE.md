# Test Coverage Summary

This document outlines all tests for verifying the `entityidentity` package data and functionality.

## Test Files

### 1. `test_import.py` - Basic Functionality Tests
Quick smoke tests that verify basic API works:

| Test | Purpose |
|------|---------|
| `test_import()` | Package can be imported |
| `test_normalize_name()` | Name normalization works |
| `test_match_company()` | Basic matching returns results |
| `test_resolve_company()` | Resolution returns proper structure |
| `test_list_companies()` | Company listing works |
| `test_load_companies()` | Database loads successfully |

**Purpose**: Fast sanity checks for package installation

---

### 2. `test_data_resolution.py` - Comprehensive Data Tests
Rigorous tests that verify data quality and entity resolution:

#### TestDataAvailability Class
Verifies the package includes proper company data:

| Test | Verification |
|------|-------------|
| `test_database_loads_successfully()` | Database loads without errors and contains data |
| `test_database_has_required_columns()` | Required columns present (name, country, name_norm) |
| `test_database_has_multiple_countries()` | International data from multiple countries (US, GB, AU, CA, DE) |
| `test_database_size_reasonable()` | At least 100+ companies included |

#### TestEntityResolution Class
Tests actual entity resolution with known companies:

| Test | Verification |
|------|-------------|
| `test_resolve_major_us_tech_company()` | Can resolve "Apple", "Apple Inc", "Apple Inc." to Apple |
| `test_resolve_company_variations()` | Different name forms resolve to same entity (Microsoft variations) |
| `test_resolve_with_full_details()` | Full resolution returns complete data structure |

#### TestNormalization Class
Verifies name normalization quality:

| Test | Verification |
|------|-------------|
| `test_normalize_removes_legal_suffixes()` | Removes Inc, Ltd, Corporation, etc. |
| `test_normalize_handles_case_and_punctuation()` | Case-insensitive, handles punctuation |

#### TestCountryFiltering Class
Tests geographic filtering:

| Test | Verification |
|------|-------------|
| `test_list_companies_by_country()` | Can filter by country code |
| `test_multiple_countries_available()` | Multiple countries have data available |

#### TestSearchFunctionality Class
Verifies search capabilities:

| Test | Verification |
|------|-------------|
| `test_search_by_name()` | Search by name terms returns relevant results |
| `test_combined_country_and_search()` | Can combine country + search filters |

#### TestMatchingQuality Class
Ensures matching quality is reasonable:

| Test | Verification |
|------|-------------|
| `test_high_confidence_matches_have_high_scores()` | Well-known companies get high scores (>70) |
| `test_no_match_for_garbage_input()` | Garbage input doesn't incorrectly match |

#### TestDataSources Class
Verifies data from multiple sources:

| Test | Verification |
|------|-------------|
| `test_has_lei_data()` | LEI data is included |
| `test_has_multiple_data_sources()` | Data from multiple countries/sources (5+ countries) |

**Purpose**: Comprehensive verification that package data enables real entity resolution

---

## Running the Tests

### Quick Test (Recommended)
```bash
./run_tests.sh
```

### All Tests
```bash
pytest -v
```

### Specific Test Suites
```bash
# Basic tests only
pytest tests/test_import.py -v

# Comprehensive data tests only
pytest tests/test_data_resolution.py -v
```

### Specific Test Classes
```bash
# Run only data availability tests
pytest tests/test_data_resolution.py::TestDataAvailability -v

# Run only entity resolution tests
pytest tests/test_data_resolution.py::TestEntityResolution -v
```

### Specific Test Functions
```bash
# Test a specific function
pytest tests/test_data_resolution.py::TestEntityResolution::test_resolve_major_us_tech_company -v
```

## Test Statistics

- **Total Test Files**: 2
- **Total Test Functions**: 23
- **Test Classes**: 7 (in comprehensive suite)
- **Coverage Areas**: 8 (import, normalization, matching, resolution, filtering, search, quality, data sources)

## What Gets Verified

✅ Package installation and imports  
✅ Database loads with proper structure  
✅ Contains 100+ companies from 5+ countries  
✅ Successfully resolves major companies (Apple, Microsoft)  
✅ Handles name variations correctly  
✅ Normalization removes legal suffixes  
✅ Country filtering works  
✅ Search functionality returns relevant results  
✅ High confidence for real companies  
✅ Low confidence for garbage input  
✅ LEI data included  
✅ Multiple data sources present  

## Success Criteria

For a successful installation and data package verification:

1. ✅ All tests in `test_import.py` pass (6/6)
2. ✅ At least 80% of tests in `test_data_resolution.py` pass (14+/17)
3. ✅ Can resolve at least one major company (Apple or Microsoft)
4. ✅ Database contains 100+ companies from 5+ countries
5. ✅ Normalization handles legal suffixes correctly

## Known Companies Tested

These well-known companies are used in tests:
- **Apple Inc** (US Tech)
- **Microsoft Corporation** (US Tech)
- **BHP Group** (AU Mining)
- **Tesla** (US Auto/Tech)

If the package can resolve these variations correctly, entity resolution is working properly.

