# Example 4: Dry Run Preview & Collision Handling

This example demonstrates how to preview changes and handle file conflicts.

## What This Example Does

1. Shows how to use `--dry-run` to preview changes
2. Demonstrates collision handling with `--on-conflict` options

## Setup

```bash
./setup.sh
```

Creates files that will cause conflicts when run twice.

## Part 1: Dry Run Preview

Preview what would happen without making changes:

```bash
python3 -m fl_classifier test_files organized --dry-run
```

You'll see log messages showing what **would** happen, but no files are actually moved.

## Part 2: Collision Handling

### First Run - Normal Operation
```bash
python3 -m fl_classifier test_files_conflict organized_conflict
```

Files are organized normally.

### Second Run - Conflicts!

Try running again with the same source files:

#### Option 1: Skip (default)
```bash
python3 -m fl_classifier test_files_conflict organized_conflict --on-conflict skip
```
Files that already exist are skipped with a warning.

#### Option 2: Rename
```bash
python3 -m fl_classifier test_files_conflict organized_conflict --on-conflict rename
```
Duplicate files are renamed: `file.txt` → `file_1.txt`

#### Option 3: Overwrite
```bash
python3 -m fl_classifier test_files_conflict organized_conflict --on-conflict overwrite
```
Existing files are replaced (use with caution!).

## Expected Output

### Dry Run
```
2026-01-22 22:00:00 - INFO - Found 5 files and 0 folders in /path/to/test_files
2026-01-22 22:00:00 - INFO - Move file: document.pdf -> Documents
2026-01-22 22:00:00 - INFO - Move file: photo.jpg -> Images
...
2026-01-22 22:00:00 - INFO - Done! Statistics:
2026-01-22 22:00:00 - INFO -   - Files classified: 5
```

### With Rename Strategy
```
organized_conflict/
├── Documents/
│   ├── document.pdf
│   ├── document_1.pdf  ← Renamed!
│   └── document_2.pdf  ← Renamed again!
└── Images/
    ├── photo.jpg
    └── photo_1.jpg     ← Renamed!
```

## What You'll Learn

1. **Safe testing** - Always preview with `--dry-run` first
2. **Conflict strategies** - Choose how to handle duplicates
3. **Rename pattern** - Files get `_1`, `_2`, etc. suffixes
4. **Log interpretation** - Understand what the tool is doing

## Try This

```bash
# 1. Setup
./setup.sh

# 2. Preview first
python3 -m fl_classifier test_files organized --dry-run

# 3. Run for real
python3 -m fl_classifier test_files organized

# 4. Create duplicates and test rename
cp test_files/* test_files_dup/
python3 -m fl_classifier test_files_dup organized --on-conflict rename

# 5. Check results
ls -R organized/
```

## Clean Up

```bash
rm -rf test_files* organized*
```

## Best Practices

✅ **DO**: Always use `--dry-run` first for important files
✅ **DO**: Use `--copy` mode to keep originals
✅ **DO**: Use `--on-conflict rename` to preserve all files

❌ **DON'T**: Use `--on-conflict overwrite` without backups
❌ **DON'T**: Skip dry-run for large operations

## Next Steps

- Review all [examples](../README.md)
- Check [troubleshooting guide](../../README.md#troubleshooting)
