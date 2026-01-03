import requests
import csv
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

fsFile = open("scrapt_quotes.csv", "w")
fsWriter = csv.writer(fsFile)
response = requests.get(url)

# check if request is successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # find all <h1> tags
    quotes = soup.find_all("span", attrs = {'class': 'text'})
    authors = soup.find_all("small", attrs = {'class': 'author'})
    

    fsWriter.writerow([ "QUOTES" , 'AUTHOR' ])
    for a, b  in zip(quotes, authors ):
        print(f'\n"quotes":{a.text}\n"authors": {b.text}')
        fsWriter.writerow([ a.text , b.text ])
        #print(title.text.strip())[]
else:
    print("Failed to retrieve page")

    fsFile.close()