#!/bin/bash
# Quick test runner script

echo "======================================"
echo "EntityIdentity Package Tests"
echo "======================================"
echo ""

# Check if package is installed
if ! python -c "import entityidentity" 2>/dev/null; then
    echo "⚠️  Warning: entityidentity package not found"
    echo "   Run: pip install -r requirements.txt"
    echo ""
    exit 1
fi

echo "✅ Package installed successfully"
echo ""

echo "Running Basic Tests..."
echo "--------------------------------------"
pytest tests/test_import.py -v
BASIC_RESULT=$?
echo ""

echo "Running Comprehensive Data Tests..."
echo "--------------------------------------"
pytest tests/test_data_resolution.py -v
DATA_RESULT=$?
echo ""

echo "======================================"
echo "Test Summary"
echo "======================================"
if [ $BASIC_RESULT -eq 0 ]; then
    echo "✅ Basic tests: PASSED"
else
    echo "❌ Basic tests: FAILED"
fi

if [ $DATA_RESULT -eq 0 ]; then
    echo "✅ Data tests: PASSED"
else
    echo "❌ Data tests: FAILED"
fi
echo ""

if [ $BASIC_RESULT -eq 0 ] && [ $DATA_RESULT -eq 0 ]; then
    echo "🎉 All tests passed!"
    exit 0
else
    echo "⚠️  Some tests failed"
    exit 1
fi

