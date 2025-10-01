#!/usr/bin/env python
"""
CLI runner for entityidentity tests
"""
import sys
import pytest


def main():
    """Run the test suite via command line"""
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-v"]
    
    # Add the tests directory to pytest args
    test_args = ["tests"] + args
    
    print("=" * 60)
    print("EntityIdentity Package Test Suite")
    print("=" * 60)
    print()
    
    exit_code = pytest.main(test_args)
    
    print()
    if exit_code == 0:
        print("✅ All tests passed!")
    else:
        print(f"❌ Tests failed with exit code: {exit_code}")
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

