# Code Line Counter

A dependency-free Python CLI that counts code, comment, and blank lines in a project and groups the results by programming language.

## Objective
Give developers a quick overview of a project's size and composition directly from the terminal.

## Need
- Project size is a basic metric used in estimation, code reviews, and reports.
- Heavy tools like cloc or SonarQube need installation and setup.
- Separating code, comments, and blank lines shows how well documented a project is.
- Students and small teams often need a simple tool to include project statistics in reports.

## Usage
```bash
python counter.py                # scan current folder
python counter.py ./my-project   # scan a specific folder
```

Example output:
```
Language     Files    Code  Comments   Blank
-------------------------------------------
Python           4     320        45      60
JavaScript       2     150        20      25
-------------------------------------------
TOTAL            6     470        65      85
```

## Run tests
```bash
python -m unittest -v
```

## Concepts demonstrated
File system traversal, data aggregation with dictionaries, formatted output, CLI design with `argparse`, unit testing.

## Future scope
Block-comment detection, JSON/CSV export, percentage breakdown, largest-files report.
