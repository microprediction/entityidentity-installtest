"""
Pytest configuration and fixtures for entityidentity tests
"""
import pytest


@pytest.fixture(scope="session")
def entityidentity_module():
    """Import and return the entityidentity module"""
    import entityidentity
    return entityidentity


@pytest.fixture(scope="session")
def company_database():
    """Load and cache the company database for tests"""
    from entityidentity import list_companies
    return list_companies()


@pytest.fixture(scope="session")
def available_countries(company_database):
    """Get list of available countries in the database"""
    if len(company_database) > 0:
        return company_database['country'].unique().tolist()
    return []


def pytest_configure(config):
    """Configure pytest with custom settings"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "requires_data: tests that require company data to be present"
    )


def pytest_report_header(config):
    """Add custom header to pytest output"""
    return [
        "EntityIdentity Installation Test Suite",
        "Testing entity resolution and data availability"
    ]

