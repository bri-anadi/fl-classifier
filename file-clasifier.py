#!/usr/bin/env python3
"""
File Classifier - Automatically classify files based on their extensions
Works on Windows, macOS, and Linux
"""

import os
import shutil
import sys
import argparse
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('file_classifier')

# File categories based on extensions
FILE_CATEGORIES = {
    # Documents
    'Documents': [
        '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls',
        '.xlsx', '.ppt', '.pptx', '.csv', '.xml', '.json', '.md'
    ],
    # Images
    'Images': [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg',
        '.webp', '.ico', '.heic', '.raw'
    ],
    # Audio
    'Audio': [
        '.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a'
    ],
    # Video
    'Videos': [
        '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm',
        '.m4v', '.mpg', '.mpeg'
    ],
    # Archives
    'Archives': [
        '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso', '.dmg'
    ],
    # Programming code
    'Code': [
        '.py', '.java', '.cpp', '.c', '.h', '.js', '.html', '.css',
        '.php', '.rb', '.go', '.rs', '.ts', '.swift', '.kt', '.sh'
    ],
    # Executables
    'Executables': [
        '.exe', '.msi', '.bin', '.bat', '.sh', '.app', '.apk', '.deb', '.rpm'
    ]
}

def classify_files(source_dir, target_dir, create_symlinks=False, dry_run=False):
    """
    Classifies files from source_dir into subfolders in target_dir
    based on file extensions.

    Args:
        source_dir (str): Source directory for files
        target_dir (str): Target directory to store classified files
        create_symlinks (bool): If True, create symlinks instead of moving/copying files
        dry_run (bool): If True, only show what would be done without actually doing it
    """
    source_path = Path(source_dir).expanduser().resolve()
    target_path = Path(target_dir).expanduser().resolve()

    # Create target directory if it doesn't exist (except in dry run)
    if not dry_run and not target_path.exists():
        target_path.mkdir(parents=True)
        logger.info(f"Created target directory: {target_path}")

    # Map extensions to categories
    extension_to_category = {}
    for category, extensions in FILE_CATEGORIES.items():
        for ext in extensions:
            extension_to_category[ext] = category

    # Get all files from the source directory
    try:
        all_files = [f for f in source_path.glob('*') if f.is_file()]
    except Exception as e:
        logger.error(f"Error reading source directory: {e}")
        return

    logger.info(f"Found {len(all_files)} files in {source_path}")

    # Counters for statistics
    stats = {
        'classified': 0,
        'unclassified': 0,
        'errors': 0,
        'skipped': 0
    }

    # Process each file
    for file_path in all_files:
        try:
            # Get extension (convert to lowercase for case-insensitive matching)
            extension = file_path.suffix.lower()

            # Determine category
            category = extension_to_category.get(extension, 'Others')

            # Create category directory if it doesn't exist
            category_path = target_path / category
            if not dry_run and not category_path.exists():
                category_path.mkdir(parents=True)
                logger.info(f"Created category directory: {category_path}")

            # Target file path
            target_file = category_path / file_path.name

            # Check if file already exists in target directory
            if target_file.exists():
                logger.warning(f"File already exists in target: {target_file}")
                stats['skipped'] += 1
                continue

            # Log action to be taken
            action = "Symlink" if create_symlinks else "Move"
            logger.info(f"{action} {file_path.name} ({extension}) -> {category}")

            if not dry_run:
                if create_symlinks:
                    # Create symlink
                    target_file.symlink_to(file_path)
                else:
                    # Move file
                    shutil.move(str(file_path), str(target_file))

            stats['classified'] += 1

        except Exception as e:
            logger.error(f"Error processing {file_path.name}: {e}")
            stats['errors'] += 1

    # Display statistics
    logger.info(f"Done! Statistics:")
    logger.info(f"  - Files classified: {stats['classified']}")
    logger.info(f"  - Files skipped: {stats['skipped']}")
    logger.info(f"  - Errors: {stats['errors']}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Classify files based on their extensions")
    parser.add_argument("source", help="Source directory containing files")
    parser.add_argument("target", nargs="?", default="./classified",
                        help="Target directory (default: ./classified)")
    parser.add_argument("-l", "--symlinks", action="store_true",
                        help="Create symlinks instead of moving files")
    parser.add_argument("-c", "--copy", action="store_true",
                        help="Copy files instead of moving them")
    parser.add_argument("-d", "--dry-run", action="store_true",
                        help="Show what would be done without actually doing it")

    args = parser.parse_args()

    # Confirm operation if not a dry run
    if not args.dry_run:
        operation = "copy" if args.copy else "create symlinks to" if args.symlinks else "move"
        print(f"This will {operation} files from '{args.source}' to '{args.target}'")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation canceled.")
            return

    # If copy option is selected, override the method used
    if args.copy:
        original_move = shutil.move
        shutil.move = shutil.copy2
        logger.info("Mode: Copying files (not moving)")

    try:
        classify_files(args.source, args.target, args.symlinks, args.dry_run)
    except KeyboardInterrupt:
        logger.info("Operation stopped by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        # Restore original function if it was changed
        if args.copy:
            shutil.move = original_move

if __name__ == "__main__":
    main()
