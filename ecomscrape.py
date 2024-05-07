import requests
from bs4 import BeautifulSoup
import pandas as pd

names_list = []
prices_list = []
desc_list = []
reviews_list = []

for i in range(1, 11):
    url = 'https://www.flipkart.com/search?q=mobile+under+5000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+5000%7CMobiles&requestId=cb049f5d-22a2-4e00-bc18-2929fbf4758f&as-backfill=on'+str(i)
    r = requests.get(url)
    print(r)

    # Parsing
    soup = BeautifulSoup(r.text, "lxml")

    # Find the main container that holds all the products
    box = soup.find("div", class_='DOjaWF gdgoEp')

    if box:
        names = box.find_all('div', class_='KzDlHZ')
        for i in names:
            n = i.text
            names_list.append(n)
        print(names_list)

        # Prices Section
        prices = box.find_all("div", class_='Nx9bqj _4b5DiR')
        for i in prices:
            p = i.text
            prices_list.append(p)
        print(prices_list)

        # Description Section
        desc = box.find_all('ul', class_='G4BRas')
        for i in desc:
            n = i.text
            desc_list.append(n)
        print(desc_list)

        # Reviews List
        reviews = box.find_all('div', class_='XQDdHH')
        for i in reviews:
            n = i.text
            reviews_list.append(n)
        print(reviews_list)

df = pd.DataFrame({"Product Name": names_list, "Product prices": prices_list, "Product description": desc_list, "Product reviews": reviews_list})


df.to_csv("mobiles.csv")
