# Example 1: Basic File Organization

This example demonstrates the most common use case: organizing files by their extensions.

## What This Example Does

Classifies mixed files into organized categories:
- Documents (PDF, TXT, DOCX)
- Images (JPG, PNG)
- Code (PY, HTML, JS)
- Archives (ZIP)
- Others (unknown extensions)

## Setup

Run the setup script to create sample files:

```bash
./setup.sh
```

This creates a `test_files/` directory with:
```
test_files/
├── report.pdf
├── notes.txt
├── presentation.pptx
├── photo.jpg
├── diagram.png
├── screenshot.png
├── script.py
├── index.html
├── styles.css
├── backup.zip
└── data.unknown
```

## Run the Example

```bash
./run.sh
```

Or manually:
```bash
python -m fl_classifier test_files organized
```

## Expected Output

```
organized/
├── Documents/
│   ├── report.pdf
│   ├── notes.txt
│   └── presentation.pptx
├── Images/
│   ├── photo.jpg
│   ├── diagram.png
│   └── screenshot.png
├── Code/
│   ├── script.py
│   ├── index.html
│   └── styles.css
├── Archives/
│   └── backup.zip
└── Others/
    └── data.unknown
```

## What You'll Learn

1. **Basic classification** - Files are automatically sorted by extension
2. **Category mapping** - See how extensions map to categories
3. **Unknown files** - Files with unrecognized extensions go to "Others"

## Try Different Options

### Preview first (dry-run)
```bash
python -m fl_classifier test_files organized --dry-run
```

### Copy instead of move
```bash
python -m fl_classifier test_files organized --copy
```

### Handle conflicts with rename
```bash
# Run twice to see conflict handling
python -m fl_classifier test_files organized
python -m fl_classifier test_files organized --on-conflict rename
```

## Clean Up

```bash
rm -rf test_files organized
```

## Next Steps

- Try [Example 2: Time-Based Organization](../02_time_based/)
- Learn about [collision handling](../README.md#common-patterns)
