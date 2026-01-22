# Release Guide for fl-classifier

This guide explains how to create a new release and publish to PyPI.

## Prerequisites

Before creating a release, ensure you have:

1. **PyPI Account**: Create an account at https://pypi.org
2. **GitHub Environment Setup**: Configure PyPI trusted publishing
3. **All changes committed**: Ensure all code changes are committed and pushed

## PyPI Trusted Publishing Setup

### Step 1: Configure PyPI Trusted Publisher

1. Go to https://pypi.org/manage/account/publishing/
2. Click "Add a new pending publisher"
3. Fill in the details:
   - **PyPI Project Name**: `fl-classifier`
   - **Owner**: `bri-anadi`
   - **Repository name**: `fl-classifier`
   - **Workflow name**: `python-publish.yml`
   - **Environment name**: `pypi`

### Step 2: Create GitHub Environment (Optional but Recommended)

1. Go to your GitHub repository settings
2. Navigate to **Environments** → **New environment**
3. Name it: `pypi`
4. Add protection rules if desired (e.g., required reviewers)

## Creating a Release

### Method 1: Using GitHub Web Interface (Recommended)

1. Go to https://github.com/bri-anadi/fl-classifier/releases
2. Click **"Draft a new release"**
3. Click **"Choose a tag"** → Type `v0.1.2` → Click **"Create new tag: v0.1.2 on publish"**
4. Set **Release title**: `v0.1.2`
5. In the description, paste the changelog:

```markdown
## What's Changed

### Fixed
- **Import bug**: Renamed main module from `fl-classifier.py` to `fl_classifier.py` to fix Python import issues
- **Monkey patching bug**: Removed dangerous global override of `shutil.move` in copy mode
  - Added `use_copy` parameter to `organize_by_time()` and `classify_items()` functions
  - Implemented proper conditional logic for move/copy/symlink operations
  - Fixed copy functionality for both files and folders

### Changed
- Improved action logging to show "Move", "Copy", or "Symlink" based on actual operation

**Full Changelog**: https://github.com/bri-anadi/fl-classifier/compare/v0.1.1...v0.1.2
```

6. Click **"Publish release"**

### Method 2: Using Git Command Line

```bash
# Create and push tag
git tag -a v0.1.2 -m "Release v0.1.2: Fix import and monkey patching bugs"
git push origin v0.1.2

# Then create release on GitHub web interface using the tag
```

## What Happens After Release

Once you publish the release on GitHub:

1. **GitHub Actions triggers** the `python-publish.yml` workflow
2. **Build step** creates distribution packages (wheel and source)
3. **PyPI publish step** uploads to PyPI using trusted publishing
4. **Package available** at https://pypi.org/project/fl-classifier/

## Monitoring the Release

1. Go to **Actions** tab in your GitHub repository
2. Find the "Upload Python Package" workflow run
3. Monitor the progress:
   - ✅ `release-build` job should complete first
   - ✅ `pypi-publish` job should publish to PyPI

## Verifying the Release

After successful publication:

```bash
# Install from PyPI
pip install fl-classifier==0.1.2

# Verify installation
fl-classifier --help

# Or use Python
python -m fl_classifier --help
```

## Troubleshooting

### Issue: PyPI publish fails with authentication error

**Solution**: Ensure PyPI trusted publishing is configured correctly:
- Check the workflow name matches exactly: `python-publish.yml`
- Verify environment name is `pypi`
- Confirm repository owner and name are correct

### Issue: Build fails

**Solution**: Test build locally first:
```bash
pip install build
python -m build
```

### Issue: Tag already exists

**Solution**: Delete and recreate the tag:
```bash
git tag -d v0.1.2
git push origin :refs/tags/v0.1.2
git tag -a v0.1.2 -m "Release v0.1.2"
git push origin v0.1.2
```

## Future Releases

For future releases:

1. Update version in:
   - `pyproject.toml`
   - `src/fl_classifier/__init__.py`
2. Update `CHANGELOG.md`
3. Commit changes
4. Create new release with appropriate version tag
5. GitHub Actions will automatically publish to PyPI

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (0.1.0): New features, backward compatible
- **PATCH** (0.1.1): Bug fixes, backward compatible
