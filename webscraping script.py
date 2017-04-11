# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 09:19:10 2017

@author: Graham
"""
from fastcache import clru_cache
import requests_cache as rc
import requests as requests
from bs4 import BeautifulSoup
import lxml.html as ix
from urllib2 import Request, urlopen


url = 'https://www.theguardian.com/politics'

@clru_cache(maxsize=128,typed=False)
def getLinks(url):
    
    a = requests.get(url)
    r = a.text
    soup = BeautifulSoup(r, 'html.parser')
    links = [x.findNext().get('href') for x in soup.findAll('h2')]

    return(links)

@clru_cache(maxsize=128,typed=False)
def linkExtract(url, page=None):
    
    #SETS THE DEFAULT NUM_PAGES TO 1
    if page is None:
        page=1
    
    #SETS INDEXING FOR WHEN PAGE NUMBER IS 0
    num_pages = range(1, page + 1)
    
    #CREATE SEARCH QUERY FOR EACH PAGE TO BE SEARCHED
    query = [(url + '?page=' + str(x)) for x in num_pages]
    
    #GET THE LINKS FOR EVERY PAGE
    links = [getLinks(x) for x in query]
    
    return(links)

def infoGet(url):
    
    #OPEN THE URL SO IT CAN BE READ
    url_opened = urlopen(url)
    
    #PARSE IT
    soup = BeautifulSoup(url_opened, 'html.parser')
    
    #ALL THE INFO WE WANT IS IN '<div itemprop=articleBody>' SO WE PULL IT OUT AND MAKE IT A STRING
    article = str([j.text for j in soup.findAll("div") if j.get("itemprop") == "articleBody"])
    
    #THERE ARE SEVERAL PLACES TO PULL THE ARTICLE TITLE, BUT WE'RE GETTING IT FROM '<h1 class=entry-title>'
    title = soup.find_all('h1', {'class':'entry-title'})[0].text
    
    #AUTHOR CAN BE FOUND AT THE END OF THE PARAGRAPH, FOLLOWED ONLY BY URL SO WITH TWO SPLITS WE CAN PULL IT OUT, MAKING
    #SURE TO IGNORE THE ASCII CHARACTERS. SET ANY PROBLEM FIELDS TO NaN
    try:
        author = re.split('Written [Bb]y:*', article, re.IGNORECASE)[1].encode('ascii', 'ignore')
        author = re.split('\\\\', author, re.IGNORECASE)[0].encode('ascii', 'ignore')
    except:
        author = np.NaN
     
    #TEXT OF THE ARTICLE IS ALL IN <p> TAGS WITH 'font-weight: 400' SO ITS EASY TO PULL OUT
    paragraphs = [soup.find_all("span", { "style" : "font-weight: 400;" })[j].text 
                  for j in range(len(soup.find_all("span", { "style" : "font-weight: 400;" })))]
    
    #REMOVE THE ASCII CHARACTERS AND JOIN THE PARAGRAPHS TOGETHER
    text = "".join(paragraphs).encode('ascii', 'ignore')
    
    #COMBINE INTO A DICTIONARY
    dic = {'author': author, 'text': text, 'title': title, 'url': url}
    
    return(dic)