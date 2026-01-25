# File Classifier

A powerful, cross-platform Python utility for organizing files and folders automatically based on extensions, folder names, or timestamps.

[![PyPI version](https://badge.fury.io/py/fl-classifier.svg)](https://pypi.org/project/fl-classifier/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fl-classifier.svg)](https://pypi.org/project/fl-classifier/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/fl-classifier)](https://pepy.tech/project/fl-classifier)
[![GitHub stars](https://img.shields.io/github/stars/bri-anadi/fl-classifier.svg)](https://github.com/bri-anadi/fl-classifier/stargazers)

[![EN](https://img.shields.io/badge/lang-English-blue.svg)](./README.md)
[![ID](https://img.shields.io/badge/lang-Indonesia-red.svg)](./translations/README.id.md)
[![FR](https://img.shields.io/badge/lang-France-orange.svg)](./translations/README.fr.md)
[![ES](https://img.shields.io/badge/lang-Spanish-yellow.svg)](./translations/README.es.md)
[![ZH](https://img.shields.io/badge/lang-Mandarin-teal.svg)](./translations/README.zh.md)

## Features

- **Multiple Classification Methods**:
  - **Extension-based**: Classifies files into categories based on their extensions
  - **Time-based**: Organizes files by creation, modification, or access time
  - **Folder classification**: Categorizes folders based on common naming patterns

- **File Categories**:
  - Documents (PDF, DOC, TXT, etc.)
  - Images (JPG, PNG, GIF, etc.)
  - Audio (MP3, WAV, FLAC, etc.)
  - Videos (MP4, AVI, MKV, etc.)
  - Archives (ZIP, RAR, 7Z, etc.)
  - Code (PY, JAVA, HTML, etc.)
  - Executables (EXE, MSI, APP, etc.)
  - Others (for extensions not in the above categories)

- **Folder Categories**:
  - Projects: For development and project-related folders
  - Backups: For backup and archived content
  - Documents: For document and report folders
  - Media: For photos, videos, music folders
  - Downloads: For download folders
  - Applications: For software and apps
  - Data: For datasets and databases
  - Web: For web-related content
  - Dated: For folders with date patterns (auto-detected)
  - Versioned: For folders with version patterns (auto-detected)
  - Uncategorized: For folders that don't match any patterns

- **Operation Modes**:
  - Move (default): Moves files/folders to target directories
  - Copy: Creates copies instead of moving
  - Symlink: Creates symbolic links to original files/folders
  - Dry-run: Shows what would happen without making changes

- **Cross-Platform Compatibility**:
  - Works on Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher
- No additional libraries required (uses standard library only)

## Installation

If you have the source code, you can run it as a module:

```bash
python -m fl_classifier [options]
```

## Usage

### Basic Usage

```bash
python -m fl_classifier SOURCE_DIR [TARGET_DIR]
```

If `TARGET_DIR` is not specified, files will be organized in a new directory called `./classified`.

### Common Options

```
-l, --symlinks       Create symlinks instead of moving files
-c, --copy           Copy files instead of moving them
-d, --dry-run        Show what would be done without actually doing it
-f, --folders        Include folders in the classification
```

### Classification Methods

```
-e, --extensions     Classify by file extensions (default behavior)
-t, --time           Organize by time attribute
```

### Time-based Organization Options

```
--time-attr {modified,created,accessed}
                     Time attribute to use (default: modified)
--time-format FORMAT
                     Time format for directories (default: '%Y-%m' for year-month)
```

### Collision Handling Options

```
--on-conflict {skip,rename,overwrite}
                     How to handle file conflicts (default: skip)
                     - skip: Skip files that already exist
                     - rename: Rename new files (file.txt → file_1.txt)
                     - overwrite: Replace existing files
```

## Examples

See the [examples/](examples/) directory for detailed, runnable examples:

1. **[Basic Organization](examples/01_basic_organization/)** - Classify files by extension
2. **[Time-Based](examples/02_time_based/)** - Organize by modification date
3. **[Copy Mode](examples/03_copy_mode/)** - Copy instead of move
4. **[Dry Run & Conflicts](examples/04_dry_run/)** - Preview and handle duplicates

### Quick Examples

### Extension-based Organization

```bash
# Classify all files in Downloads folder by extension
python -m fl_classifier ~/Downloads ~/Organized

# Classify files and folders, create copies instead of moving
python -m fl_classifier ~/Documents ~/Organized -f -c

# Create symlinks instead of moving files
python -m fl_classifier ~/Pictures ~/Organized -l

# Preview what would happen without making any changes
python -m fl_classifier ~/Desktop -d
```

### Time-based Organization

```bash
# Organize files by their modification time (year-month)
python -m fl_classifier ~/Documents ~/TimeOrganized -t

# Organize by creation date with year-month-day format
python -m fl_classifier ~/Photos ~/Chronological -t --time-attr created --time-format "%Y-%m-%d"

# Organize files and folders by access time
python -m fl_classifier ~/Downloads ~/AccessOrganized -t --time-attr accessed -f
```

## Troubleshooting

### Issue: Files are being skipped

**Cause**: Files already exist in target directory

**Solution**: Files with the same name in the target will be skipped by default. Check the logs for "already exists" warnings.

### Issue: Want to preview changes first

**Solution**: Use `--dry-run` flag to see what would happen without making changes:
```bash
python -m fl_classifier ~/Downloads ~/Organized --dry-run
```

### Issue: Permission denied errors

**Cause**: Insufficient permissions to read source or write to target directory

**Solution**:
- Check directory permissions
- Run with appropriate user privileges
- Ensure target directory is writable

### Issue: Symlinks not working on Windows

**Cause**: Symlink creation requires administrator privileges on Windows

**Solution**: Run terminal as administrator, or use `--copy` mode instead

## FAQ

**Q: What happens if a file or folder already exists in the target directory?**
A: By default, the script will skip it and log a warning message. The file will remain in the source directory.

**Q: Can I undo the organization?**
A: Currently, there's no built-in undo feature. We recommend:
- Use `--dry-run` first to preview changes
- Use `--copy` mode to keep original files
- Keep backups of important directories

**Q: Will the organization preserve the directory structure?**
A: No, all files are flattened to the corresponding category directories. For hierarchical organization, consider using the time-based organization with a hierarchical format like `%Y/%m/%d`.

**Q: Can I customize file categories?**
A: Yes, you can edit the `FILE_CATEGORIES` dictionary in the script to add or modify categories. Configuration file support is planned for future releases.

**Q: Does it work on Windows?**
A: Yes! The tool uses Python's `pathlib` for cross-platform compatibility and works on Windows, macOS, and Linux.

**Q: Can I organize files in subdirectories?**
A: Currently, only files in the top level of the source directory are processed. Recursive mode is planned for future releases.

**Q: How do I install the package?**
A: Install via pip:
```bash
pip install fl-classifier
```

Then run with:
```bash
fl-classifier ~/Downloads ~/Organized
# or
python -m fl_classifier ~/Downloads ~/Organized
```

## License

This utility is released under the MIT License. Feel free to use, modify, and distribute it.
