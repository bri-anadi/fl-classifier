# fl-classifier Examples

This directory contains practical examples demonstrating different use cases of fl-classifier.

## Quick Start

Each example includes:
- **README.md** - Detailed explanation
- **setup.sh** - Script to create sample files
- **run.sh** - Script to run the example

## Examples

### [01. Basic File Organization](01_basic_organization/)
Learn how to classify files by their extensions into organized categories.

**Use case**: Organize a messy Downloads folder

```bash
cd 01_basic_organization
./setup.sh  # Create sample files
./run.sh    # Run classification
```

### [02. Time-Based Organization](02_time_based/)
Organize files by their modification date into year-month folders.

**Use case**: Archive photos or documents by date

```bash
cd 02_time_based
./setup.sh
./run.sh
```

### [03. Copy Mode](03_copy_mode/)
Copy files instead of moving them, keeping originals intact.

**Use case**: Create organized copies while preserving original structure

```bash
cd 03_copy_mode
./setup.sh
./run.sh
```

### [04. Dry Run Preview](04_dry_run/)
Preview what would happen before making any changes.

**Use case**: Test classification before committing

```bash
cd 04_dry_run
./setup.sh
./run.sh
```

## Common Patterns

### Handle File Conflicts

```bash
# Skip existing files (default)
fl-classifier ~/Downloads ~/Organized --on-conflict skip

# Rename duplicates (file.txt → file_1.txt)
fl-classifier ~/Downloads ~/Organized --on-conflict rename

# Overwrite existing files
fl-classifier ~/Downloads ~/Organized --on-conflict overwrite
```

### Organize with Folders

```bash
# Include folders in classification
fl-classifier ~/Projects ~/Organized -f
```

### Create Symlinks

```bash
# Create symbolic links instead of moving
fl-classifier ~/Documents ~/Organized -l
```

## Tips

1. **Always test with `--dry-run` first**
2. **Use `--copy` mode for important files**
3. **Check logs for skipped or error files**
4. **Customize categories by editing `FILE_CATEGORIES` in source**

## Need Help?

- Check the [main README](../README.md)
- See [troubleshooting guide](../README.md#troubleshooting)
- Open an [issue](https://github.com/bri-anadi/fl-classifier/issues)
