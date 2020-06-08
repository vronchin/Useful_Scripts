# extract table from the class attribute 
from pandas.io.html import read_html
page = 'https://www.ft.com/content/691390ca-53d9-11ea-90ad-25e377c0ee1f?fbclid=IwAR3TfgUYCgwsZLN-ad-GnFN7lUcUEurB86SHRHVJewO6ZkL3XrwMGjxzJm4'

tables = read_html(page, attrs={"class":"o-table"})

file_name = './my_file.csv'

tables[0].to_csv(file_name, sep=',')

print ("Extracted {num} lines".format(num=len(tables)))

print(tables)

#
# Exemple avec beautiful SOUP puis conversion en dataframe
#

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# website_url = requests.get('https://www.ft.com/content/691390ca-53d9-11ea-90ad-25e377c0ee1f?fbclid=IwAR3TfgUYCgwsZLN-ad-GnFN7lUcUEurB86SHRHVJewO6ZkL3XrwMGjxzJm4').text

# soup = BeautifulSoup(website_url,'lxml')

# My_table = soup.find('table',{'class':'o-table o-table--row-stripes o-table--compact o-table--responsive-overflow o-table--sortable'})

# links = My_table.findAll('a')

# events = []
# for link in links:
#     events.append(link.get('title'))

# df = pd.DataFrame()
# df['events'] = events

# print(df)