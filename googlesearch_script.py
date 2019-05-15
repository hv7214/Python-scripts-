import requests, sys, webbrowser, bs4
from bs4 import BeautifulSoup

print('Googling...')

#downloading the html file
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

#converting html file into nested str(basically categorizing it )
soup = BeautifulSoup(res.text, 'html.parser')

#Limitign pages to 5
linkElem = soup.select('.r a')
numOpen = min(5, len(linkElem))

#opening pages
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElem[i].get('href'))