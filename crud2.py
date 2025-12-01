
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
        print(f"RSM Error writing file: {e}")
    except Exception as e: #4
        print(f"RSM Error An unexpected error occurred: {e}")
    #4
#2

def fReadCsv(filename): #2
    """Reads a CSV file and returns the data as a list of dictionaries."""
    
    # Check if the file exists before trying to read it
    if not os.path.exists(filename):#3
        print(f"RSM Error: File '{filename}' not found.")
        return []
    #3  
    data_list = []
    
    print(f"\n--- Reading data from {filename} ---")
    
    try: #4
        # Use 'r' mode (read) and 'encoding="utf-8"'
        with open(filename, mode='r', encoding='utf-8') as csvfile: #5
            
            # csv.DictReader maps the values in each row to the fieldnames in the first row.
            reader = csv.DictReader(csvfile)
            
            #print(f"\ndebug {reader= }")

            # The reader is an iterator, so we convert it to a list
            for row in reader: #
                #print(f"\ndebug {row= }")

                data_list.append(row)
            #    
        return data_list
    #5

    except IOError as e: #4
        print(f"RSM Error reading file: {e}")
        return []
    #4

#2
def fSell(pSellData, pProductData, pLastIdKey):#2
    subSell = {'idKey': '', 'date': '', 'id': '', 'item': '', 'pcs': '', 'amount': ''}
    pLastIdKey = int(pLastIdKey) + 1
    subSell['idKey'] = pLastIdKey
    totalAmount = 0
    pastDate = False
    while(True): #25
        #not i assume that pLastIdKey s lowest value in empty is 0
        
        if pastDate == False: #23
        #date input process
            while(True) :#7

                strInp = input('\ninput date: ')

                if strInp == "":#
                    print('blank is not valid...')
                    continue    
                #
                subSell['date'] = strInp
                break
            #7
        #23
        #BOOKMARK
        #id and item input, process
        ret = 0
        breakId = False
        while(True): #8

            strInp = input('\nselect what to input i id\nt item:  ')

            if strInp.upper() == 'I':#12
                
                while(True): #11
                    strInpTwo = input('\ninput id: ')
                    if strInpTwo == "": #10
                        print("\nblank is not valid...")
                        continue
                    #10
                    print("\ndebug strInpTwo ", strInpTwo)
                    ret = fFindData(strInpTwo, 0, pProductData)
                    if(ret == -1): #14
                        print("\ndid not found the ", strInpTwo)
                        continue
                    #14
                    subSell['id'] = strInpTwo
                    subSell['item'] = pProductData[ret]['item']
                    breakId = True
                    break
                #11

            elif strInp.upper() == 'T':#12
                
                while(True): #11
                    strInpTwo = input('\ninput item:  ')
                    if strInpTwo == "": #10
                        print("\nblank is not valid...")
                        continue
                    #10
                    ret = fFindData(strInpTwo, 1, pProductData)
                    if(ret == -1): #14
                        print("\ndid not found the ", strInpTwo)
                        continue
                    #14
                    subSell['item'] = strInpTwo
                    subSell['id'] = pProductData[ret]['id']
                    breakId = True
                    break
                #11

            #12
            if breakId == True:#22
                break
            #22
        #8

        #pcs process
        while(True) :#7

            strInp = input('\ninput pcs: ')

            if strInp == "" or int(strInp) == 0: #10
                print('blank is not valid and non numeric and 0 is not valid...')
                continue    
            #10
            subSell['pcs'] = int(strInp)
            subSell['amount'] = f"{float( pProductData[ret]['amount'] ) * float(strInp):.2f}" 
            totalAmount = float( totalAmount)  + float(subSell['amount'])   
            break   
        #7
        
        print(f"the result {subSell}")
        
        #question if will save and leave
        while(True):#22
            
            strQue = input('\ndo you want to add another transaction Y or N')
            if strQue == "": #21
                print("\nnot a valid input ")
            #21

            if strQue.upper() == 'Y':#23
                #//pProductData.append(subSell.copy() )
                pastDate = True
                break
            #23
        
            if strQue.upper() == 'N':#23
                #save and exiting prog
                subSell['totalAmount'] = totalAmount
                #//pProductData.append(subSell.copy() )
                return
            
            #23
        
        #22
        
    #25 
       
#2

def fFindData(pCompare, pKey, pData, pStartInd = 0) : #2
    #BOOKMARK
    if len(pData) == 0: #3
        return -1
    #3


    i = pStartInd 
    for sDict in pData: #4
        j = 0
        for keys in sDict: #5
            if int(pKey) == j: #7
                 
                #print("\ndebug sDict[keys] ", sDict[keys], " pCompare ", pCompare)
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
#print the whole set of data with prompt
#assuming that array of dict will be given but 1 dimension only
def fPrintData(pData = [], pPrompt = "", pLen = 0):#2

    print(pPrompt)
    for keys in pData[0]:#5
        print(keys + "     ", sep = "",end = "")
    #5
    print("")
    for vDict in pData:#3
        for keys in vDict:#4
            print(vDict[keys] + "     ", sep = "", end = "")
        #4
        print("")
    #3
#2
def fMain( ): #2

    #assuming all data accepts empty and have load, null and undefined assume will not enter
    sellData = []
    productData = []

    productData = fReadCsv('product.csv')
    sellData = fReadCsv('sell.csv')
    
    print(f"productData{productData}\nsellData{sellData}")
    while(True):#3

        print("\n#################\nSell Menu\ns sell\nv view\nq to quit: ")
        ch = input("input:  ")

        if ch.upper() == 'S': #4
            #BOOKMARK
            fSell(sellData, productData, len(productData))
                              
        elif ch.upper() == 'V': #4
            #BOOKMARK
            fPrintData(pLen = len(sellData), pData = sellData, pPrompt = "\nthis is sellData views ")
                              
        #4
        elif ch.upper() == 'Q':#4
            break
        #4
    #3
#2

fMain()


