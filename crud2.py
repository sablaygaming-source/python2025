
import csv
import os
from typing import List, Dict, Any
DataList = List[Dict[str, Any]]

def fWriteCsv(filename: str, data: DataList) -> None: #2
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
    #all_keys = set()
    #for row_dict in data:
        # Add all keys from the current dictionary to the set (to ensure uniqueness)
        all_keys.update(row_dict.keys())

    # Convert the set of keys to a list, which DictWriter requires
    #fieldnames = list(all_keys)
    
    # Optional: Sort keys alphabetically for predictable column order
    # fieldnames.sort() 
    if len(data) == 0: #11
        print("\nRSM error must not input blank")
        return 
    #11
    
    fieldnames = []
    for keys in data[0]: #5
        fieldnames.append(keys) 
    #5

    print(f"Detected Fieldnames: {fieldnames}")
    #print(f"--- Writing data to {filename} ---")

    try: #4
        # Use 'w' mode, newline="", and utf-8 encoding
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:#7
            
            # Create a DictWriter object with the dynamically generated fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row
            writer.writeheader()
            
            # Write all data rows. DictWriter automatically handles missing keys 
            # in a row by leaving the corresponding cell blank.
            writer.writerows(data)
        #7
            
        print(f"Successfully wrote {len(data)} records to {filename}.")

    except IOError as e: #4
        print(f"Error writing file: {e}")
    except Exception as e: #4
        print(f"An unexpected error occurred: {e}")
    #4
#2

def fReadCsv(filename): #2
    """Reads a CSV file and returns the data as a list of dictionaries."""
    
    # Check if the file exists before trying to read it
    if not os.path.exists(filename):#3
        print(f"Error: File '{filename}' not found.")
        return []
    #3  
    data_list = []
    
    print(f"\n--- Reading data from {filename} ---")
    
    try: #4
        # Use 'r' mode (read) and 'encoding="utf-8"'
        with open(filename, mode='r', encoding='utf-8') as csvfile: #5
            
            # csv.DictReader maps the values in each row to the fieldnames in the first row.
            reader = csv.DictReader(csvfile)
            
            # The reader is an iterator, so we convert it to a list
            for row in reader: #
                data_list.append(row)
            #    
        return data_list
    #5

    except IOError as e: #4
        print(f"Error reading file: {e}")
        return []
    #4

#2
def fSell(pSellData, pAddData):#2
    subSell = {'idKey': '', 'date': '', 'id': '', 'item': '', 'pcs': '', 'amount': ''}
    #date input process
    while(True) :#7

        strInp = input('input date: ')

        if strInp == "":#
            print('blank is not valid...')
            continue    
        #
        subSell['date'] = strInp
        break
    #7

    #id and item input, process
    while(True): #8

        strInp = input('select what to input i id\nn name:  ')

        if strInp.upper() == 'I':#
            
            while(True): #11
                strInpTwo = input('\ninput id: ')
                if strInpTwo == "": #10
                    print("\nblank is not valid...")
                    continue
                #10

            #11

        elif strInp.upper() == 'N':#
            print("part of menu ")
        #
        #subSell['date'] = ch
    #8

#2

def fFindData(pCompare, pKey, pData, pStartInd = 0) : #2

    if len(pData) == 0: #3
        return -1
    #3

    i = 0 
    for sDict in pData: #4
        j = 0
        for keys in sDict: #5
            if pKey == j: #7
                 if sDict[keys] == pCompare:#8
                    #get the target
                    return i 
                #8
            #7
            j+=1
        #5  
        i +=1      
    #4

    #didnot found any
    return -1
#2

def fMain( ): #2

    sellData = []
    productData = []

    productData = fReadCsv('product.csv')
    sellData = fReadCsv('sell.csv')
    
    print(f"productData{productData}\nsellData{sellData}")
    while(True):#3

        print("\n#################\nSell Menu\ns sell\nv view\nq to quit: ")
        ch = input("input:  ")

        if ch.upper() == 'S': #4

            ret = fFindData( "joy", 1, productData )
            print(f"\ndebug {productData[ret]= }, {ret= }")
            
            
            #a test of sell.csv

            testData = [];
            testData.append({'idKey': '1', 'date': '11/29/2025', 'id': '2', 'item': 'pride', 'pcs': '1', 'amount': '11', 'totalAmount': ''})
            testData.append({'idKey': '1', 'date': '11/29/2025', 'id': '3', 'item': 'safeguard', 'pcs': '2', 'amount': '24', 'totalAmount': '23'})
            testData.append(testData[1].copy())
            
            testData[2]['totalAmount'] = '59'
            
            fWriteCsv('sell.csv',testData)
            #fSell(sellData, productData)
            pass                   
        #4
        elif ch.upper() == 'Q':#4
            break
        #4
    #3
#2

fMain()


