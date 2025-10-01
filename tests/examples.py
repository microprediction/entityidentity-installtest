"""
Example usage of entityidentity package
"""

def example_basic_matching():
    """Example: Simple company matching"""
    from entityidentity import match_company
    
    # Find best match
    match = match_company("Apple Inc", country="US")
    if match:
        print(f"Matched: {match['name']}")
        print(f"Country: {match['country']}")
        print(f"LEI: {match.get('lei', 'N/A')}")


def example_full_resolution():
    """Example: Full resolution with details"""
    from entityidentity import resolve_company
    
    # Get full resolution details
    result = resolve_company("BHP Group", country="AU")
    
    print(f"Best match: {result['final']}")
    print(f"Decision: {result['decision']}")
    print(f"All matches: {len(result['matches'])} found")
    
    for match in result['matches'][:3]:
        print(f"  - {match['name']} (score: {match['score']})")


def example_normalize():
    """Example: Name normalization"""
    from entityidentity import normalize_name
    
    names = [
        "Apple Inc.",
        "BHP Group Ltd",
        "Microsoft Corporation",
        "Tesla, Inc."
    ]
    
    print("Name normalization:")
    for name in names:
        normalized = normalize_name(name)
        print(f"  {name} -> {normalized}")


def example_list_companies():
    """Example: List and filter companies"""
    from entityidentity import list_companies
    
    # List top 10 US companies
    us_companies = list_companies(country="US", limit=10)
    print(f"\nFound {len(us_companies)} US companies:")
    for _, company in us_companies.head(5).iterrows():
        print(f"  - {company['name']}")
    
    # Search for mining companies
    mining = list_companies(search="mining", limit=5)
    print(f"\nFound {len(mining)} mining companies:")
    for _, company in mining.iterrows():
        print(f"  - {company['name']} ({company['country']})")


def example_list_and_filter():
    """Example: List database and custom filtering"""
    from entityidentity import list_companies
    
    # List full database
    companies = list_companies()
    print(f"\nTotal companies in database: {len(companies)}")
    
    # Custom filtering
    tech_companies = companies[
        companies['name_norm'].str.contains('tech', na=False)
    ]
    print(f"Companies with 'tech' in name: {len(tech_companies)}")


if __name__ == "__main__":
    print("=" * 50)
    print("EntityIdentity Package Examples")
    print("=" * 50)
    
    try:
        print("\n1. Basic Matching")
        print("-" * 50)
        example_basic_matching()
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        print("\n2. Full Resolution")
        print("-" * 50)
        example_full_resolution()
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        print("\n3. Name Normalization")
        print("-" * 50)
        example_normalize()
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        print("\n4. List Companies")
        print("-" * 50)
        example_list_companies()
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        print("\n5. List and Filter")
        print("-" * 50)
        example_list_and_filter()
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 50)
    print("Examples completed!")
    print("=" * 50)

