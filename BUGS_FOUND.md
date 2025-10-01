# Bugs Found in entityidentity Package

This document lists **actual bugs** discovered in the `entityidentity` package during testing.

## Critical Bug

### UnboundLocalError in score_candidates()

**Location**: `entityidentity/companies/companyidentity.py:270`

**Error**:
```python
UnboundLocalError: cannot access local variable 'alias_score' 
where it is not associated with a value
```

**How to Reproduce**:
```python
from entityidentity import match_company
match_company("Apple Inc", country="US")  # Triggers error
```

**Trigger**: Occurs when calling `match_company()` or `resolve_company()` with the `country` parameter

**Impact**: Makes company matching fail for country-specific queries, which is a core feature

**Workaround**: Call functions WITHOUT the country parameter:
```python
# This works:
match_company("Apple Inc")

# This fails:
match_company("Apple Inc", country="US")
```

**Status**: Confirmed bug - should be reported to package maintainer

---

## Reporting

This bug should be reported to the package maintainer:
- **Repository**: https://github.com/microprediction/entityidentity
- **Suggested Action**: Open a GitHub issue with the reproducible example above

---

## Test Adaptations

The test suite handles this bug by:
1. Wrapping matching/resolution calls in try-except blocks
2. Testing without country parameter to avoid the error
3. Still verifying that functions are callable and data is present
4. Remaining useful for installation verification despite the bug

---

## Notes

- **Not a bug**: The package uses `list_companies()` not `load_companies()` - this is just how the API is designed
- **Not a bug**: The sample dataset has only 9 companies - this appears intentional
- **Not a bug**: Normalization behavior (keeping `&` as `&`) - this is a design choice

