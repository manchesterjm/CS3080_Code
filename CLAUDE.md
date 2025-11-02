# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a CS3080 (Python Programming) course repository containing standalone Python scripts and two main task assignments. The codebase consists of utility scripts, course exercises, and two comprehensive task projects that demonstrate web scraping and data processing with Excel.

## Running Scripts

All scripts are standalone Python files. To run any script:

```bash
python <script_name>.py
```

Most scripts are designed to be run directly without command-line arguments. Some scripts (like `file_rename.py`, `image_compare.py`, `remove_PDF_page.py`) contain hardcoded directory paths that should be modified before running.

## Key Dependencies

The repository uses the following Python packages (most commonly used across multiple scripts):

- **openpyxl** (version 3.1.2) - Excel file manipulation
- **beautifulsoup4** (bs4) - Web scraping and HTML parsing
- **requests** - HTTP requests for web scraping
- **PIL/Pillow** - Image processing
- **pygame** - Game development (in pygame_files directory)
- **PyPDF2** - PDF manipulation
- **imagehash** - Image comparison

Install dependencies as needed:
```bash
pip install openpyxl beautifulsoup4 requests pillow pygame PyPDF2 imagehash
```

## Project Structure

### Main Task Projects

**Task_1/** - Word guessing game with web scraping
- `main.py` - Scrapes top 1000 English words, stores in Excel, implements Hangman-style game
- Creates `1000_words.xlsx` when run
- Source: https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/

**Task_2/** - Author publication analysis
- `main.py` - Scrapes CVPR conference papers (2021-2023), finds top 3 authors, generates publication statistics
- Creates `authors.xlsx` with year-by-year publication counts and totals
- Source URLs are hardcoded for CVPR 2021, 2022, 2023

### Utility Scripts

- **file_rename.py** - Renames files in a directory using their modification timestamp
- **image_compare.py** - Finds duplicate images using perceptual hashing, displays side-by-side for deletion decision
- **randomize_mp3_list_for_car.py** - Randomizes MP3 files and adds numbered prefixes
- **remove_randomize_mp3.py** - Removes numeric prefixes from MP3 files
- **reorder_mp3s.py** - Reorders MP3 files
- **remove_PDF_page.py** - Removes first page from PDF files
- **update_json_files.py** - Batch updates JSON files (renames "item" to "id" in result blocks)

### Course Exercise Files

Files named with dates (e.g., `20_mar_2024.py`, `in_class_28_feb_2024.py`) are in-class exercises and homework assignments.

### Django Subdirectory

`django/` contains a Django project setup (`myworld/`) with standard Django virtual environment structure. This is a separate web development component of the course.

## Important Notes

1. **Hardcoded Paths**: Many utility scripts contain hardcoded Windows file paths (e.g., `D:\Pictures\Wallpapers`, `G:\\`). These must be modified before running.

2. **Version Checking**: Task projects check for openpyxl version 3.1.2 and warn if different versions are detected.

3. **File Creation**: Scripts in Task_1 and Task_2 delete existing Excel files before creating new ones to avoid conflicts.

4. **Web Scraping**: Both main tasks rely on specific HTML structures of their target websites. If websites change structure, the BeautifulSoup selectors may need updating.

5. **Error Handling**: Task projects implement HTTP error handling for web requests and exit with error codes on failure.

6. **Pygame Files**: The `pygame_files/` directory contains learning exercises for pygame including basic movement, text display, and a snake game implementation.

## Testing

There is no formal test suite. Scripts are designed to be run directly for validation. The `test.py` and `test.json` files in the root are minimal test fixtures, not comprehensive test suites.
