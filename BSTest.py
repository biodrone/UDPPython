from bs4 import BeautifulSoup
import urllib2

def checker():
    url = "http://176.31.191.50/index.html"
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)

    print(len(soup.a.string)) #gets the length of the first name
    
checker()