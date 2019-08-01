#! python3
#lucky.py

import requests, sys, webbrowser, bs4

print('Googling...') # disaplys text while downloading google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# retrieve top search reult for links.
soup = bs4.BeautifulSoup(res.text)
# open a browser tab for each result.
linkElems = soup.select('div r') #finds all <a> elemnts that are within an element that has the r CSS class.
numOpen = min(5, len(linkElems)) #opens 5 search results, the length of the list of returns, if fewer than 5.
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
