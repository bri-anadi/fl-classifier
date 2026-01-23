# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-01-23

### Added
- **Collision handling**: New `--on-conflict` parameter with three strategies:
  - `skip`: Skip files that already exist (default)
  - `rename`: Automatically rename duplicates (file.txt → file_1.txt)
  - `overwrite`: Replace existing files
- **Examples directory**: Added 4 comprehensive examples with runnable scripts:
  - Basic file organization by extension
  - Time-based organization
  - Copy mode usage
  - Dry-run and collision handling
- **Badges**: Added PyPI version, Python versions, license, downloads, and GitHub stars badges to README
- **Documentation improvements**:
  - Expanded FAQ section with 8 common questions
  - Added troubleshooting section with 4 common issues
  - Added collision handling options documentation
  - Added examples section with links to detailed guides

### Changed
- Improved logging messages to show conflict actions (renamed/overwritten/created)
- Enhanced README with better organization and more examples
- Updated help text to include collision handling options

### Fixed
- Better handling of duplicate files in target directory
- Improved error messages for file conflicts

## [0.1.3] - 2026-01-22

### Added
- **`__main__.py`**: Added support for running package as a module with `python -m fl_classifier`

## [0.1.2] - 2026-01-22

### Fixed
- **Import bug**: Renamed main module from `fl-classifier.py` to `fl_classifier.py` to fix Python import issues
- **Monkey patching bug**: Removed dangerous global override of `shutil.move` in copy mode
  - Added `use_copy` parameter to `organize_by_time()` and `classify_items()` functions
  - Implemented proper conditional logic for move/copy/symlink operations
  - Fixed copy functionality for both files (using `shutil.copy2`) and folders (using `shutil.copytree`)

### Changed
- Improved action logging to show "Move", "Copy", or "Symlink" based on actual operation

## [0.1.1] - 2026-01-XX

### Added
- Initial release with file and folder classification features
- Support for extension-based and time-based organization
- Multiple operation modes: move, copy, symlink, dry-run
- Cross-platform compatibility (Windows, macOS, Linux)
- Internationalization support (EN, ID, FR, ES, ZH)

[0.1.2]: https://github.com/bri-anadi/fl-classifier/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/bri-anadi/fl-classifier/releases/tag/v0.1.1
