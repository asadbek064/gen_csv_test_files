# Generate CSV Test Files

A simple script to generate a suite of CSV files for testing data import/export.

## Usage

```bash
uv sync
uv run main.py
```

## Generated Files

The `test_files` directory will be populated with files to test specific scenarios, including:

*   **Basic Delimiters:** Comma, tab, and pipe-separated files.
*   **Header Variations:** Files with no headers, duplicate headers, and invalid characters in headers.
*   **Special Characters:** Files with quoted fields, mixed-case data, and long strings.
*   **Missing Data:** Files with empty cells and blank lines.
*   **Numeric Formats:** Files with scientific notation and European decimal formats.
*   **Edge Cases:** Files with a single column, a single row, and many columns.
---

Created by Asadbek Karimov ([asadk.dev](https://asadk.dev) | contact@asadk.dev)