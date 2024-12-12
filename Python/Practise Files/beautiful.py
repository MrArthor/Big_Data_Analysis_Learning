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

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())

# Remove Superfluous Data (unnecessary data)

import requests
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

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
    
# Export data i CSV

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Create a file to write to, add headers row
f = csv.writer(open('myfile1.csv', 'w'))
f.writerow(['Name', 'Link'])

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')


    # Add each artist’s name and associated link to a row
    f.writerow([names, links])
    pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)
    
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links])
 
#
import sys 
import urllib.request 
  
# Save a reference to the original 
# standard output 
original_stdout = sys.stdout 
  
# as an example, taken my article list 
# published link page and stored in local 
with urllib.request.urlopen('https://nielit.gov.in/content/contact-us-1') as webPageResponse: 
    outputHtml = webPageResponse.read() 
  
# Scraped contents are placed in  
# samplehtml.html file and getting 
# used for next set of examples 
with open('samplehtml.html', 'w') as f: 
      
    # Here the  standard output is  
    # written to the file that we  
    # used above 
    sys.stdout = f 
    print(outputHtml) 
      
    # Reset the standard output to its  
    # original value 
    sys.stdout = original_stdout  
    
# Importing BeautifulSoup and  
# it is in the bs4 module 
from bs4 import BeautifulSoup 
  
# Opening the html file. If the file 
# is present in different location,  
# exact location need to be mentioned 
HTMLFileToBeOpened = open("samplehtml.html", "r") 
  
# Reading the file and storing in a variable 
contents = HTMLFileToBeOpened.read() 
  
# Creating a BeautifulSoup object and 
# specifying the parser  
beautifulSoupText = BeautifulSoup(contents, 'lxml') 
  
  
# Using the prettify method to modify the code 
#  Prettify() function in BeautifulSoup helps 
# to view about the tag nature and their nesting 
print(beautifulSoupText.body.prettify()) 