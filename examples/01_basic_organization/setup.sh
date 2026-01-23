#!/bin/bash
# Setup script for basic organization example

echo "Creating test files..."

# Create test directory
mkdir -p test_files

# Create sample documents
echo "Sample PDF content" > test_files/report.pdf
echo "Sample notes" > test_files/notes.txt
echo "Sample presentation" > test_files/presentation.pptx

# Create sample images
echo "Sample image" > test_files/photo.jpg
echo "Sample diagram" > test_files/diagram.png
echo "Sample screenshot" > test_files/screenshot.png

# Create sample code files
cat > test_files/script.py << 'EOF'
#!/usr/bin/env python3
print("Hello, World!")
EOF

cat > test_files/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body><h1>Hello</h1></body>
</html>
EOF

cat > test_files/styles.css << 'EOF'
body {
    font-family: Arial, sans-serif;
}
EOF

# Create sample archive
echo "Sample archive" > test_files/backup.zip

# Create unknown file type
echo "Unknown data" > test_files/data.unknown

echo "✅ Created test files in test_files/"
echo ""
echo "Files created:"
ls -1 test_files/
echo ""
echo "Run ./run.sh to classify these files"
