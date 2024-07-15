import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"

req = requests.get(url)
content = BeautifulSoup(req.content, "html.parser")

#  'tUxRFH' class contains the product info and 

data = content.find_all('div', {'class': 'tUxRFH'})

links = []
phn_name = []
start_link = "https://www.flipkart.com"

for items in data:
    rest_link = items.find('a')['href']
    # 'KzDlHZ' contains the phone names
    name = items.find('div', attrs={'class': 'KzDlHZ'}) 
    if name:
        phn_name.append(name.text)
        links.append(start_link + rest_link)

if len(phn_name) > 0:
    print(phn_name[1])
    print(links[1])
else:
    print("No phone names found.")

dataframe = {
        'Phone Name': phn_name,
        'Link': links
    }
    # Create a DataFrame from the dictionary
final_dataframe = pd.DataFrame(dataframe)
print(final_dataframe)

#importing alldata into csv file
final_dataframe.to_csv('FK_Data_url.csv')
