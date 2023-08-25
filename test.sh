#!/bin/bash
coverage run -m unittest discover -s tests -p "test_*.py"

# Generate coverage report
coverage report -m

# Calculate coverage percentage
coverage_percentage=$(coverage report | tail -n 1 | awk '{print $4}')

echo "coverage: $coverage_percentage"