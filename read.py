import csv
import os

CSV_FILE_NAME = 'user_records.csv'

def read_csv_to_list_of_dicts(filename):
    """Reads a CSV file and returns the data as a list of dictionaries."""
    
    # Check if the file exists before trying to read it
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return []

    data_list = []
    
    print(f"\n--- Reading data from {filename} ---")
    
    try:
        # Use 'r' mode (read) and 'encoding="utf-8"'
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            
            # csv.DictReader maps the values in each row to the fieldnames in the first row.
            reader = csv.DictReader(csvfile)
            
            # The reader is an iterator, so we convert it to a list
            for row in reader:
                data_list.append(row)
                
        return data_list

    except IOError as e:
        print(f"Error reading file: {e}")
        return []

# Execute the reading function
records = read_csv_to_list_of_dicts(CSV_FILE_NAME)

# Process and display the data
if records:
    print(f"Successfully read {len(records)} records.\nI change the string index to number by RSM")
    myKeys = ['UserID', 'Name', 'Is_Active']
    # Example: Display the data
    for record in records:
        #print(f"ID: {record['UserID']}, Name: {record['Name']}, Active: {record['Is_Active']}")
        for i in range(0,3,1):
            print(f"{ myKeys[i]}: {record[myKeys[0]]} ", end ="")
        print("")          
    # Example: Access a specific record's data
    print(f"\nName of the second user: {records[1]['Name']}")