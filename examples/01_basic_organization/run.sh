#!/bin/bash
# Run script for basic organization example

echo "Running fl-classifier on test files..."
echo ""

# Check if test_files exists
if [ ! -d "test_files" ]; then
    echo "❌ test_files directory not found!"
    echo "Run ./setup.sh first to create sample files"
    exit 1
fi

# Run classifier
python3 -m fl_classifier test_files organized

echo ""
echo "✅ Classification complete!"
echo ""
echo "Check the 'organized' directory to see results:"
echo ""

# Show organized structure
if [ -d "organized" ]; then
    echo "organized/"
    for dir in organized/*/; do
        if [ -d "$dir" ]; then
            dirname=$(basename "$dir")
            echo "├── $dirname/"
            for file in "$dir"*; do
                if [ -f "$file" ]; then
                    filename=$(basename "$file")
                    echo "│   ├── $filename"
                fi
            done
        fi
    done
fi

echo ""
echo "To clean up: rm -rf test_files organized"
