import csv
import os

# 1. Define the data as a List of Dictionaries
# This mirrors how you would typically work with records in a database or API response.
user_data = [
    {'UserID': 101, 'Name': 'Alice Johnson', 'Email': 'alice@example.com', 'Is_Active': True},
    {'UserID': 102, 'Name': 'Bob Smith', 'Email': 'bob@example.com', 'Is_Active': False},
    {'UserID': 103, 'Name': 'Charlie Brown', 'Email': 'charlie@example.com', 'Is_Active': True},
    # Note: If a dictionary is missing a key, DictWriter will leave that cell blank (by default).
    {'UserID': 104, 'Name': 'Dana Scully', 'Email': 'dana@example.com'}, 
]

CSV_FILE_NAME = 'user_dictionary_records.csv'

# 2. Define the Fieldnames (Column Headers)
# These MUST match the keys in your dictionaries exactly.
fieldnames = ['UserID', 'Name', 'Email', 'Is_Active', 'Notes'] 
# I added 'Notes' to show how DictWriter handles missing keys (it fills them with empty strings)

print(f"--- Writing data (from list of dicts) to {CSV_FILE_NAME} ---")

try:
    # Use 'w' mode, newline="", and encoding="utf-8" for robust writing
    with open(CSV_FILE_NAME, mode='w', newline='', encoding='utf-8') as csvfile:
        
        # Create a DictWriter object
        # It takes the file object and the list of fieldnames (keys)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # 3. Write the Header Row
        # This uses the 'fieldnames' list provided above.
        writer.writeheader()
        print("Header written successfully.")
        
        # 4. Write all data rows
        # writerows() takes the list of dictionaries and maps keys to columns.
        writer.writerows(user_data)
        
    print(f"Successfully wrote {len(user_data)} records to CSV.")

except IOError as e:
    print(f"Error writing file: {e}")

# Verification: Print the content of the generated file
print("\n--- Generated File Content ---")
if os.path.exists(CSV_FILE_NAME):
    with open(CSV_FILE_NAME, 'r', encoding='utf-8') as f:
        print(f.read())