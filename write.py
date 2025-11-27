import csv
import os

# 1. Define the filename and data
CSV_FILE_NAME = 'user_records.csv'
data_to_write = [
    # Header row (mandatory for structured data)
    ['UserID', 'Name', 'Email', 'Is_Active'],
    
    # Data rows
    [1, 'Alice Johnson', 'alice@example.com', True],
    [2, 'Bob Smith', 'bob@example.com', False],
    [3, 'Charlie Brown', 'charlie@example.com', True],
]

print(f"--- Writing data to {CSV_FILE_NAME} ---")

try:
    # Use 'w' mode (write) and 'newline=""' to prevent blank rows on Windows.
    # 'encoding="utf-8"' ensures special characters are handled correctly.
    with open(CSV_FILE_NAME, mode='w', newline='', encoding='utf-8') as csvfile:
        
        # Create a writer object
        csv_writer = csv.writer(csvfile)
        
        # Use writerows() to write the entire list of lists at once
        csv_writer.writerows(data_to_write)
        
    print(f"Successfully wrote {len(data_to_write) - 1} records (plus header).")

except IOError as e:
    print(f"Error writing file: {e}")

# Verification: Print the content of the generated file
print("\n--- Generated File Content ---")
if os.path.exists(CSV_FILE_NAME):
    with open(CSV_FILE_NAME, 'r', encoding='utf-8') as f:
        print(f.read())