import csv
import os
from typing import List, Dict, Any

# Define a flexible type hint for clarity
DataList = List[Dict[str, Any]]

def write_dicts_to_csv(filename: str, data: DataList) -> None:
    """
    Writes a list of dictionaries to a CSV file.
    
    Dynamically determines the fieldnames (column headers) by finding 
    all unique keys present across all dictionaries in the data list.
    
    Args:
        filename: The path to the CSV file to be created or overwritten.
        data: A list of dictionaries, where each dictionary is a row.
    """
    if not data:
        print("Error: Input data list is empty. Cannot write CSV.")
        return

    # --- 1. Dynamically determine the fieldnames (column headers) ---
    all_keys = set()
    for row_dict in data:
        # Add all keys from the current dictionary to the set (to ensure uniqueness)
        all_keys.update(row_dict.keys())

    # Convert the set of keys to a list, which DictWriter requires
    fieldnames = list(all_keys)
    
    # Optional: Sort keys alphabetically for predictable column order
    # fieldnames.sort() 
    
    print(f"Detected Fieldnames: {fieldnames}")
    print(f"--- Writing data to {filename} ---")

    try:
        # Use 'w' mode, newline="", and utf-8 encoding
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            
            # Create a DictWriter object with the dynamically generated fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row
            writer.writeheader()
            
            # Write all data rows. DictWriter automatically handles missing keys 
            # in a row by leaving the corresponding cell blank.
            writer.writerows(data)
            
        print(f"Successfully wrote {len(data)} records to {filename}.")

    except IOError as e:
        print(f"Error writing file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- EXAMPLE USAGE ---

# Example 1: Standardized Data
data_set_a = [
    {'Product_ID': 'A1', 'Name': 'Laptop', 'Price': 1200.00},
    {'Product_ID': 'A2', 'Name': 'Monitor', 'Price': 350.50},
]
write_dicts_to_csv('products_a.csv', data_set_a)


# Example 2: Data with varying keys (This demonstrates the power of dynamic key detection)
data_set_b = [
    # Row 1 has 'Location'
    {'ID': 10, 'Status': 'Open', 'Location': 'New York'},
    # Row 2 is missing 'Location' but has 'Notes'
    {'ID': 11, 'Status': 'Closed', 'Notes': 'Urgent repair needed'},
    # Row 3 has all keys
    {'ID': 12, 'Status': 'Pending', 'Location': 'Boston', 'Notes': 'Follow up next week'},
]
write_dicts_to_csv('dynamic_tickets.csv', data_set_b)


# --- Verification: Print the content of the generated files ---

print("\n--- Content of dynamic_tickets.csv ---")
if os.path.exists('dynamic_tickets.csv'):
    with open('dynamic_tickets.csv', 'r', encoding='utf-8') as f:
        print(f.read())