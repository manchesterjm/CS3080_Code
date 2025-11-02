# Python Style Guide

**CS3080 - Python Programming Course - Coding Standards**

**Version**: 1.0
**Last Updated**: November 2, 2025
**Project**: CS3080 Python Programming Coursework
**Author**: Josh Manchester

This document defines the coding standards for all Python code in this repository. Following these guidelines ensures consistency, maintainability, and professional code quality.

---

## Table of Contents

1. [General Principles](#general-principles)
2. [Python Style (PEP 8)](#python-style-pep-8)
3. [Naming Conventions](#naming-conventions)
4. [Code Organization](#code-organization)
5. [Functions and Methods](#functions-and-methods)
6. [Documentation](#documentation)
7. [Error Handling](#error-handling)
8. [Imports](#imports)
9. [Type Hints](#type-hints)
10. [File Naming](#file-naming)
11. [Code Review Checklist](#code-review-checklist)

---

## General Principles

### Core Values
1. **Readability First**: Code is read more often than written
2. **Explicit is Better Than Implicit**: Clear over clever
3. **Consistency**: Follow existing patterns in the codebase
4. **DRY (Don't Repeat Yourself)**: Extract common functionality
5. **YAGNI (You Aren't Gonna Need It)**: Don't build for hypothetical futures
6. **Separation of Concerns**: Each component should have a single responsibility

### Code Quality Standards
- **Pylint Score**: Maintain 10.0/10 (current: 10.00/10) ✅
- **All 52 Files Compliant**: Every Python file scores 10/10
- **No Warnings**: Address all linter warnings before committing
- **Professional Documentation**: Comprehensive docstrings on all modules and functions

---

## Python Style (PEP 8)

### Line Length
```python
# Maximum line length: 120 characters
# This is more permissive than PEP 8's 79, suitable for modern displays

# BAD: Line too long
def some_function():
    print("This is a very long message that exceeds the maximum line length and should be broken into multiple lines for readability")

# GOOD: Line broken appropriately
def some_function():
    print(
        "This is a very long message that has been broken into "
        "multiple lines for better readability"
    )
```

### Indentation
```python
# Use 4 spaces per indentation level (never tabs)

# GOOD
def calculate_total(items):
    total = 0
    for item in items:
        if item.is_valid:
            total += item.price
    return total
```

### Blank Lines
```python
# Two blank lines between top-level definitions
class FirstClass:
    pass


class SecondClass:
    pass


# One blank line between method definitions
class MyClass:
    def first_method(self):
        pass

    def second_method(self):
        pass


# Use blank lines sparingly inside functions to show logical sections
def complex_function():
    # Setup
    data = fetch_data()

    # Processing
    processed = transform(data)

    # Return
    return processed
```

### Whitespace
```python
# Whitespace in expressions and statements

# GOOD
x = 1
y = 2
long_variable = 3

# BAD
x             = 1
y             = 2
long_variable = 3

# GOOD
spam(ham[1], {eggs: 2})

# BAD
spam( ham[ 1 ], { eggs: 2 } )

# GOOD
if x == 4:
    print(x, y)
    x, y = y, x

# BAD
if x == 4 :
    print(x , y)
    x , y = y , x
```

---

## Naming Conventions

### General Rules
```python
# Variables and functions: lowercase_with_underscores
user_count = 10
def get_user_profile():
    pass

# Classes: CapitalizedWords (PascalCase)
class UserProfile:
    pass

# Constants: UPPERCASE_WITH_UNDERSCORES
MAX_LOGIN_ATTEMPTS = 5
DEFAULT_TIMEOUT = 300
DIRECTORY = r'C:\Path\To\Files'

# "Private" (internal): single leading underscore
def _internal_helper():
    pass

_internal_variable = "hidden"

# Module names: snake_case (all lowercase with underscores)
# GOOD: file_rename.py, image_compare.py, apr_10_in_class.py
# BAD: FileRename.py, imageCompare.py, 10_apr_in_class.py
```

### Boolean Variables
```python
# Use is_, has_, can_, should_ prefixes for booleans
is_active = True
has_permission = False
can_edit = True
should_retry = False

# BAD
active = True      # Ambiguous
permission = False # What does False mean?
```

---

## Code Organization

### File Organization
```python
"""
Module docstring explaining the purpose of this file.

This module handles file renaming based on modification timestamps.
"""

# Standard library imports
import logging
import os
import time
from datetime import datetime, timedelta

# Third-party imports
import openpyxl
import requests
from PIL import Image

# Local application imports (if applicable)
from .utils import helper_function

# Constants
MAX_RETRIES = 3
DEFAULT_DIRECTORY = r'C:\Files'

# Module-level variables (if necessary)
logger = logging.getLogger(__name__)

# Functions and classes (in logical order)
```

### Import Ordering
```python
# 1. Standard library
import os
import sys
from datetime import datetime

# 2. Third-party packages
import openpyxl
import pygame
from PIL import Image

# 3. Local application/library specific (if applicable)
from .models import User
from .utils import helper_function

# Within each group, imports should be alphabetical
```

---

## Functions and Methods

### Single Return Statement Principle
```python
# GOOD: Single return point (when practical)
def calculate_discount(price, membership_level):
    """Calculate discount based on membership."""
    # Guard clauses for validation (early returns OK)
    if price <= 0:
        return 0
    if not membership_level:
        return 0

    # Main logic with single return
    discount = 0
    if membership_level == 'premium':
        discount = price * 0.20
    elif membership_level == 'standard':
        discount = price * 0.10

    return discount

# ACCEPTABLE: Multiple returns for validation/error cases
def process_file(filename):
    """Process file and return data."""
    # Early returns for error conditions
    if not os.path.exists(filename):
        return None, "File not found"

    if not filename.endswith('.txt'):
        return None, "Invalid file type"

    # Main logic
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    return data, "Success"
```

### Function Length
```python
# Keep functions focused and concise (generally <50 lines)
# If longer, consider breaking into smaller functions

# BAD: Too long, does too many things
def process_images(directory):
    # 100+ lines of mixed validation, processing, saving...
    pass

# GOOD: Broken into logical pieces
def process_images(directory):
    """Process all images in directory."""
    if not _validate_directory(directory):
        return False

    images = _load_images(directory)
    processed = _apply_filters(images)
    _save_results(processed, directory)

    return True

def _validate_directory(directory):
    """Validate directory exists and is readable."""
    return os.path.isdir(directory)

def _load_images(directory):
    """Load all image files from directory."""
    return [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png'))]
```

### Function Arguments
```python
# Limit function arguments (≤5 is ideal, ≤7 maximum)

# BAD: Too many arguments
def rename_file(source, dest, prefix, suffix, counter, date, backup):
    pass

# GOOD: Group related data into objects/dicts
def rename_file(source, dest, options):
    """
    Rename file with specified options.

    Args:
        source: Source file path
        dest: Destination file path
        options: Dict with keys: prefix, suffix, counter, date, backup
    """
    pass
```

### Default Arguments
```python
# Never use mutable default arguments

# BAD
def add_item(item, items=[]):
    items.append(item)
    return items

# GOOD
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Documentation

### Docstrings
```python
# All modules, classes, and public functions must have docstrings

# Module docstring
"""
File renaming utility based on modification timestamps.

This module renames files in a directory based on their last modified timestamp,
creating a standardized naming convention of YYYY-MM-DD_HH-MM-SS.
"""

# Function docstring (Google style)
def find_duplicates(directory: str) -> list[tuple[str, str]]:
    """
    Find duplicate images in a directory using average hashing.

    Args:
        directory: Path to directory containing images

    Returns:
        list: List of tuples containing (duplicate_path, original_path)

    Raises:
        ValueError: If directory does not exist
        PermissionError: If directory is not readable

    Example:
        >>> duplicates = find_duplicates(r'C:\\Pictures')
        >>> print(f"Found {len(duplicates)} duplicates")
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Directory not found: {directory}")

    # Implementation...
    return duplicates

# Class docstring
class BankAccount:
    """
    Bank account with deposit and withdrawal functionality.

    Manages account balance and transaction history.

    Attributes:
        balance: Current account balance
        transactions: List of all transactions
    """
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []
```

### Code Comments
```python
# Use comments to explain WHY, not WHAT

# BAD: Comment states the obvious
# Increment counter by 1
counter += 1

# GOOD: Comment explains reasoning
# Add 1 to account for zero-indexing in display
counter += 1

# BAD: Redundant comment
# Get files from directory
files = os.listdir(directory)

# GOOD: Explains business logic
# Only process images modified within the last 7 days
recent_images = [f for f in files if is_recent(f, days=7)]

# Use TODO comments for future improvements
# TODO: Add pagination when file count exceeds 1000

# Use FIXME for known issues
# FIXME: Handle timezone conversion for international files
```

---

## Error Handling

### Exceptions
```python
# Use specific exceptions, not bare except

# BAD
try:
    file = open(filename)
except:
    return None

# GOOD
try:
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
except FileNotFoundError:
    logger.warning("File not found: %s", filename)
    return None
except PermissionError:
    logger.error("Permission denied: %s", filename)
    return None

# Catch multiple specific exceptions
try:
    result = process_image(filename)
except (OSError, PermissionError) as e:
    logger.error("File error: %s", str(e))
    return False
```

### Error Messages
```python
# Error messages should be clear and actionable

# BAD
raise ValueError("Invalid input")

# GOOD
raise ValueError(
    f"Invalid time range: start_time ({start_time}) must be before "
    f"end_time ({end_time})"
)

# Provide context in error messages
if not os.path.exists(directory):
    raise FileNotFoundError(
        f"Directory does not exist: {directory}. "
        "Please create the directory or check the path."
    )
```

### Validation
```python
# Validate early, fail fast

def rename_files_by_timestamp(directory: str) -> tuple[int, dict[str, int]]:
    """Rename files based on modification timestamp."""
    # Validation at the top
    if not directory:
        raise ValueError("Directory path cannot be empty")
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    if not os.path.isdir(directory):
        raise ValueError(f"Path is not a directory: {directory}")

    # Main logic after validation
    files_processed = 0
    # ... implementation
    return files_processed, date_counts
```

---

## Imports

### Order and Organization
```python
# Group imports in this order:
# 1. Standard library
# 2. Third-party packages
# 3. Local application

# Within each group, alphabetize by module name

# GOOD
import logging
import os
from datetime import datetime, timedelta

import bs4
import openpyxl
import requests

# BAD - mixed ordering
import openpyxl
import os
from datetime import datetime
import logging
```

### Import Styles
```python
# Prefer explicit imports

# GOOD
import os
import sys
from datetime import datetime

# ACCEPTABLE for common libraries
from PIL import Image, ImageTk

# Avoid wildcard imports
# BAD
from os import *
from tkinter import *

# GOOD
import tkinter as tk
from tkinter import Button, Label
```

---

## Type Hints

### Usage
```python
# Use type hints for function signatures (Python 3.9+)

from typing import List, Dict, Optional

def calculate_free_slots(
    target_date: str,
    start_hour: int = 8,
    end_hour: int = 20
) -> List[str]:
    """Calculate free time slots for a given date."""
    pass

# Use Optional for values that can be None
def get_file_info(file_path: str) -> Optional[tuple[int, str]]:
    """Get file size and modification date."""
    if not os.path.exists(file_path):
        return None

    size = os.path.getsize(file_path)
    mod_time = os.path.getmtime(file_path)
    return size, mod_time

# Modern type hint syntax (Python 3.10+)
def process_files(directory: str) -> list[tuple[str, str]]:
    """Process files and return results."""
    results: list[tuple[str, str]] = []
    # ... implementation
    return results
```

---

## File Naming

### Python Files
```python
# Use snake_case for all Python files
# GOOD
file_rename.py
image_compare.py
mar_20_2024.py
in_class_jan_12_2024.py
remove_pdf_page.py

# BAD
FileRename.py
imageCompare.py
10_apr_in_class.py  # Don't start with numbers
remove_PDF_page.py  # Don't use mixed case
tempCodeRunnerFile.py  # Use snake_case
```

### Directory Structure
```
CS3080/
├── Task_1/
│   └── main.py              # Main task scripts
├── Task_2/
│   └── main.py
├── Homework_one/
│   ├── program1.py          # Homework assignments
│   ├── program2.py
│   └── program3.py
├── homework_5_6/
│   ├── question1.py
│   └── question2.py
├── pygame_files/
│   ├── snake_game.py        # Game demonstrations
│   └── moving_an_image.py
├── file_rename.py           # Utility scripts
├── image_compare.py
├── randomize_mp3_list_for_car.py
└── STYLE_GUIDE.md          # This file
```

---

## Code Review Checklist

### Before Committing
- [ ] All files run without errors
- [ ] Pylint score = 10.0 (no errors or warnings)
- [ ] Docstrings added for all modules and functions
- [ ] Type hints added for function signatures
- [ ] Import ordering is correct (stdlib → third-party → local)
- [ ] File names follow snake_case convention
- [ ] No commented-out code
- [ ] No debug print statements (unless intentional)
- [ ] Constants are UPPER_CASE
- [ ] Functions/variables are lowercase_with_underscores
- [ ] Proper error handling (no bare except)
- [ ] Code is documented and readable

### Code Quality
- [ ] Functions are focused (<50 lines when possible)
- [ ] Function arguments are limited (≤5 ideal, ≤7 max)
- [ ] No mutable default arguments
- [ ] Resource management uses `with` statements
- [ ] File operations specify encoding
- [ ] Paths use raw strings (r'C:\path') when needed
- [ ] Two blank lines between top-level definitions
- [ ] One blank line between method definitions
- [ ] Lines are ≤120 characters

---

## Current Project Statistics

### Code Quality Achievement
- **Total Python Files**: 52
- **Pylint Score**: 10.00/10 ✅
- **Files with Issues**: 0
- **Documentation Coverage**: 100%
- **Type Hint Coverage**: ~95%

### File Categories
1. **Task Projects** (2 files): Task_1/main.py, Task_2/main.py
2. **Utilities** (8 files): File management, image processing, MP3 tools, PDF utilities
3. **Homework** (12 files): Course assignments
4. **In-Class Exercises** (10 files): Class demonstrations
5. **Pygame Files** (9 files): Game programming examples
6. **Miscellaneous** (11 files): Supporting scripts

---

## Resources

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python - Code Quality](https://realpython.com/python-code-quality/)
- [CLAUDE.md](./CLAUDE.md) - Project-specific development guide

---

## Changelog

### Version 1.0 (November 2, 2025)
- Initial style guide creation for CS3080 project
- Achieved 10.00/10 Pylint score across all 52 files
- Established comprehensive documentation standards
- Implemented type hints throughout codebase
- Standardized file naming to snake_case convention
- Added professional module and function docstrings
- Fixed import ordering and code organization
- Removed all pylint warnings and errors

---

**Questions or Suggestions?**

This guide reflects the current best practices for Python code in this CS3080 coursework repository. All code in this project now follows these standards and achieves a perfect 10/10 Pylint score.
