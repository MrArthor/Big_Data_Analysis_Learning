#pip install requests
#pip install html5lib
#pip install bs4

import requests
URL = "https://www.timeanddate.com/worldclock/usa/new-york"
req = requests.get(URL)
print(req.content)

#extract the title from the webpage −
from bs4 import BeautifulSoup
import requests
url = "https://www.timeanddate.com/worldclock/usa/new-york"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)

#extract all the URLs within a webpage
for link in soup.find_all('a'):
 print(link.get('href'))

# Pull text from a web page using beautiful soap

import requests
from bs4 import BeautifulSoup

# Collect first page of artists’ list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText 
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())
# Pretify is use to visualize and understand the structure of HTML and XML documents. 
# Remove Superfluous Data (unnecessary data)

import requests
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')
soup  # print the data extract from webpage
pg=soup.find(class_='BodyText')
pg
# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links
last_links.decompose() #used to remove a tag from the parse tree. 

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.prettify())
    
    
# pull out the content from webpage

import requests
from bs4 import BeautifulSoup
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Use .contents to pull out the <a> tag’s children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)
    
# Export data in CSV

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Create a file to write to, add headers row
f = csv.writer(open('E:/data/myfile1.csv', 'w'))
f.writerow(['Name', 'Link'])

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
     names = artist_name.contents[0]
     links = 'https://web.archive.org' + artist_name.get('href')
     print(links)

    # Add each artist’s name and associated link to a row
     f.writerow([names, links])
     pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)
    
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        print(links)
        f.writerow([names, links])
 
