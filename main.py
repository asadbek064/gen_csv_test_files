import csv
import os

# Create a directory for the test files if it doesn't exist
output_dir = 'test_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#  1. Basic CSV Files

# Standard comma-delimited
with open(os.path.join(output_dir, 'test_basic.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age', 'salary'])
    writer.writerow([1, 'John Doe', 30, 50000])
    writer.writerow([2, 'Jane Smith', 25, 60000])
    writer.writerow([3, 'Bob Johnson', 35, 75000])

# Tab-delimited
with open(os.path.join(output_dir, 'test_tab.txt'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['id', 'name', 'age', 'salary'])
    writer.writerow([1, 'John Doe', 30, 50000])
    writer.writerow([2, 'Jane Smith', 25, 60000])
    writer.writerow([3, 'Bob Johnson', 35, 75000])

# Pipe-delimited
with open(os.path.join(output_dir, 'test_pipe.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(['id', 'name', 'age', 'salary'])
    writer.writerow([1, 'John Doe', 30, 50000])
    writer.writerow([2, 'Jane Smith', 25, 60000])
    writer.writerow([3, 'Bob Johnson', 35, 75000])

#  2. Header Variations

# No header row
with open(os.path.join(output_dir, 'test_no_headers.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([1, 'John Doe', 30, 50000])
    writer.writerow([2, 'Jane Smith', 25, 60000])
    writer.writerow([3, 'Bob Johnson', 35, 75000])

# Duplicate column names
with open(os.path.join(output_dir, 'test_duplicate_headers.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'name', 'salary', 'salary'])
    writer.writerow([1, 'John', 'Doe', 50000, 60000])
    writer.writerow([2, 'Jane', 'Smith', 60000, 70000])

# Invalid header names (spaces, special chars, starting with numbers)
with open(os.path.join(output_dir, 'test_invalid_headers.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['1st Name', 'Last Name', 'Age (years)',
                    'Salary $', 'Email@Address'])
    writer.writerow(['John', 'Doe', 30, 50000, 'john@email.com'])
    writer.writerow(['Jane', 'Smith', 25, 60000, 'jane@email.com'])

#  3. Special Characters & Quoting

# Fields with commas requiring quotes
with open(os.path.join(output_dir, 'test_quotes.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['id', 'name', 'description', 'notes'])
    writer.writerow([1, 'Doe, John', 'Product A, B, C',
                    'Contains commas, quotes'])
    writer.writerow([2, 'Smith, Jane', 'Item "Special"', 'Has "quoted" text'])
    writer.writerow([3, 'Johnson, Bob', 'Normal text', 'No special chars'])

# Mixed case data
with open(os.path.join(output_dir, 'test_mixed_case.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'NAME', 'Address', 'City'])
    writer.writerow([1, 'JOHN DOE', '123 Main St', 'NEW YORK'])
    writer.writerow([2, 'jane smith', '456 Oak Ave', 'los angeles'])
    writer.writerow([3, 'Bob Johnson', '789 Pine Rd', 'Chicago'])

#  4. Missing & Empty Values

# Missing values and empty cells
with open(os.path.join(output_dir, 'test_missing.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age', 'salary', 'department'])
    writer.writerow([1, 'John', '', 50000, ''])
    writer.writerow([2, '', 25, '', 'Sales'])
    writer.writerow([3, 'Bob', 35, 75000, 'Engineering'])
    writer.writerow([4, '', '', '', ''])
    writer.writerow([5, 'Alice', 28, 65000, 'Marketing'])

# Empty lines (manual write for precise control)
with open(os.path.join(output_dir, 'test_empty_lines.csv'), 'w', encoding='utf-8') as f:
    f.write('id,name,age\n\n1,John,30\n\n2,Jane,25\n\n3,Bob,35\n\n')

#  5. Numeric Formatting

# Various numeric formats
with open(os.path.join(output_dir, 'test_numbers.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'price', 'quantity', 'percentage', 'scientific'])
    writer.writerow([1, 1234.56, 100, 15.5, '1.23e10'])
    writer.writerow([2, 9876.54, 200, 25.75, '4.56e-5'])
    writer.writerow([3, 5000.00, 150, 33.33, '7.89e8'])

# European decimal format (comma as decimal, period as thousands)
with open(os.path.join(output_dir, 'test_decimals_eu.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'price', 'quantity'])
    writer.writerow([1, '1.234,56', 100])
    writer.writerow([2, '9.876,54', 200])
    writer.writerow([3, '5.000,00', 150])

#  6. Large Column Count

# Many columns
with open(os.path.join(output_dir, 'test_many_columns.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    headers = ['id'] + [f'col{i}' for i in range(1, 16)]
    writer.writerow(headers)
    # Row 1
    writer.writerow([1] + [chr(ord('a') + i) for i in range(15)])
    # Row 2
    writer.writerow([2] + ['p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd'])

#  7. Edge Cases

# Single column
with open(os.path.join(output_dir, 'test_single_column.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['values'])
    writer.writerow([100])
    writer.writerow([200])
    writer.writerow([300])

# Single row (header only)
with open(os.path.join(output_dir, 'test_single_row.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age', 'salary'])

# Very long text fields
with open(os.path.join(output_dir, 'test_long_strings.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'description'])
    writer.writerow([1, 'This is a very long description that contains multiple sentences and goes on for quite some time to test how the system handles longer text fields that might wrap or need special handling'])
    writer.writerow([2, 'Another extremely long piece of text with various punctuation marks!!! Including exclamation points, question marks? And lots of commas, semicolons; and other special characters @#$%'])

print(
    f"Successfully generated all test files in the '{output_dir}' directory.")
