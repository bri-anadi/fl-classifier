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
import re

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

# Folder classification keywords
FOLDER_CATEGORIES = {
    'Projects': ['project', 'proj', 'dev', 'development'],
    'Backups': ['backup', 'bak', 'old', 'archive'],
    'Documents': ['document', 'doc', 'text', 'report', 'paper'],
    'Media': ['media', 'video', 'audio', 'music', 'photo', 'picture', 'image'],
    'Downloads': ['download', 'dl'],
    'Applications': ['app', 'application', 'program', 'software'],
    'Data': ['data', 'dataset', 'database', 'db'],
    'Web': ['web', 'website', 'site', 'html']
}

def determine_folder_category(folder_name):
    """
    Determines category for a folder based on its name.

    Args:
        folder_name (str): Name of the folder to categorize

    Returns:
        str: Category name
    """
    folder_name_lower = folder_name.lower()

    # Check if folder name matches any category keywords
    for category, keywords in FOLDER_CATEGORIES.items():
        for keyword in keywords:
            if keyword in folder_name_lower:
                return category

    # If no match found, check if folder name contains numbers with specific patterns
    # Date patterns: 2023, 2023-01, etc.
    if re.search(r'\b(19|20)\d{2}\b', folder_name):
        return 'Dated'

    # Version patterns: v1.0, ver2.3, etc.
    if re.search(r'\bv(er)?\s*\d+(\.\d+)?\b', folder_name_lower):
        return 'Versioned'

    return 'Uncategorized'


def classify_items(source_dir, target_dir, create_symlinks=False, dry_run=False, classify_folders=False):
    """
    Classifies files and optionally folders from source_dir into subfolders in target_dir
    based on file extensions and folder naming patterns.

    Args:
        source_dir (str): Source directory for files and folders
        target_dir (str): Target directory to store classified items
        create_symlinks (bool): If True, create symlinks instead of moving/copying items
        dry_run (bool): If True, only show what would be done without actually doing it
        classify_folders (bool): If True, also classify folders
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

    # Get all items from the source directory
    try:
        all_files = [f for f in source_path.glob('*') if f.is_file()]
        all_folders = [f for f in source_path.glob('*') if f.is_dir()] if classify_folders else []
    except Exception as e:
        logger.error(f"Error reading source directory: {e}")
        return

    logger.info(f"Found {len(all_files)} files and {len(all_folders)} folders in {source_path}")

    # Counters for statistics
    stats = {
        'files_classified': 0,
        'folders_classified': 0,
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
            logger.info(f"{action} file: {file_path.name} ({extension}) -> {category}")

            if not dry_run:
                if create_symlinks:
                    # Create symlink
                    target_file.symlink_to(file_path)
                else:
                    # Move file
                    shutil.move(str(file_path), str(target_file))

            stats['files_classified'] += 1

        except Exception as e:
            logger.error(f"Error processing file {file_path.name}: {e}")
            stats['errors'] += 1

    # Process each folder if folder classification is enabled
    if classify_folders:
        for folder_path in all_folders:
            try:
                # Skip the target directory if it's inside the source directory
                if folder_path == target_path:
                    logger.info(f"Skipping target directory: {folder_path}")
                    continue

                # Determine category for the folder
                folder_name = folder_path.name
                category = determine_folder_category(folder_name)

                # Create category directory if it doesn't exist
                category_path = target_path / f"Folders_{category}"
                if not dry_run and not category_path.exists():
                    category_path.mkdir(parents=True)
                    logger.info(f"Created folder category directory: {category_path}")

                # Target folder path
                target_folder = category_path / folder_name

                # Check if folder already exists in target directory
                if target_folder.exists():
                    logger.warning(f"Folder already exists in target: {target_folder}")
                    stats['skipped'] += 1
                    continue

                # Log action to be taken
                action = "Symlink" if create_symlinks else "Move"
                logger.info(f"{action} folder: {folder_name} -> Folders_{category}")

                if not dry_run:
                    if create_symlinks:
                        # Create symlink
                        target_folder.symlink_to(folder_path, target_is_directory=True)
                    else:
                        # Move folder
                        shutil.move(str(folder_path), str(target_folder))

                stats['folders_classified'] += 1

            except Exception as e:
                logger.error(f"Error processing folder {folder_path.name}: {e}")
                stats['errors'] += 1

    # Display statistics
    logger.info(f"Done! Statistics:")
    logger.info(f"  - Files classified: {stats['files_classified']}")
    if classify_folders:
        logger.info(f"  - Folders classified: {stats['folders_classified']}")
    logger.info(f"  - Items skipped: {stats['skipped']}")
    logger.info(f"  - Errors: {stats['errors']}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Classify files and folders based on extensions and naming patterns")
    parser.add_argument("source", help="Source directory containing files and folders")
    parser.add_argument("target", nargs="?", default="./classified",
                        help="Target directory (default: ./classified)")
    parser.add_argument("-l", "--symlinks", action="store_true",
                        help="Create symlinks instead of moving items")
    parser.add_argument("-c", "--copy", action="store_true",
                        help="Copy items instead of moving them")
    parser.add_argument("-d", "--dry-run", action="store_true",
                        help="Show what would be done without actually doing it")
    parser.add_argument("-f", "--folders", action="store_true",
                        help="Also classify folders (not just files)")

    args = parser.parse_args()

    # Confirm operation if not a dry run
    if not args.dry_run:
        operation = "copy" if args.copy else "create symlinks to" if args.symlinks else "move"
        items = "files and folders" if args.folders else "files"
        print(f"This will {operation} {items} from '{args.source}' to '{args.target}'")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation canceled.")
            return

    # If copy option is selected, override the method used
    if args.copy:
        original_move = shutil.move
        shutil.move = shutil.copy2
        logger.info(f"Mode: Copying {'files and folders' if args.folders else 'files'} (not moving)")

    try:
        classify_items(args.source, args.target, args.symlinks, args.dry_run, args.folders)
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
