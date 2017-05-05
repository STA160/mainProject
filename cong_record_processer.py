# -*- coding: utf-8 -*-
"""
Created on Thu May 04 22:38:00 2017

@author: Graham
"""

from bs4 import BeautifulSoup
import requests_cache
import requests

# START CACHING
requests_cache.install_cache("demo_cache")

# STEP 1: RETRIEVE LIST OF URLS 

def get_links(url):
    soup = BeautifulSoup((requests.get(url)).text, "html.parser")
    companies = soup.find_all(name='li',attrs={'class':'ListingCategories_AllCategories_CATEGORY'})
    link = [x.find_all("a")[0]["href"] for x in companies]
    links = [x.encode('UTF8') for x in link]
    return ['http://web.davischamber.com' + i for i in links]
  
  # STEP 2: GET CATEGORIES
links_list = get_links('http://web.davischamber.com/davis/allcategories')
categories = [links_list[i].split('/')[-1] for i in range(len(links_list))]
print categories

# STEP 3: GET INFO (INTO A DICTIONARY)
def get_names(url):
    soup = BeautifulSoup((requests.get(url)).text, "html.parser")
    companies = soup.find_all(name='div',attrs={'class':'ListingResults_All_CONTAINER ListingResults_Level4_CONTAINER'})
    
    # CREATE A DICTIONARY WITH WANTED INFO 
    cdict = {'company':'','address':'','last_name':'','first_name':'','phone':''} 
    
    # FIND COMPANY NAME 
    the_company = [soup.find_all('div',attrs={'class':'ListingResults_All_ENTRYTITLELEFTBOX'})[i].get_text() for i in range(len(companies))] #pulls out the first element in h1
    cdict['company'] = [x.encode('UTF8') for x in the_company]
    
    # FIND COMPANY'S ADDRESS
    # addresses end in a 5 digit zip code and after the zipcode is the point of contact 
    #cdict['address'] = [soup.find_all('span',attrs={'itemprop':'street-address'})[i].get_text() for i in range(len(companies))] #pulls out the first element in h1
    all_contact_info = [soup.find_all('div',attrs={'class':'ListingResults_Level4_MAINLEFTBOX'})[i].get_text() for i in range(len(companies))] #pulls out the first element in h1
        
    # CONVERT THE UNICODE TO STRING
    contact_info = [x.encode('UTF8') for x in all_contact_info]
       
    # POINTS OF CONTACT
    poc = [contact_info[i].split('\n')[0] for i in range(len(companies))]
    
    # ADDRESSES
    cdict['address'] = [" ".join(poc[i].split()[:-2]) for i in range(len(poc))]
    
    # LAST NAME
    try:
        [poc[i].split()[-1] for i in range(len(poc)) if i != 0]
    except ValueError:
        print('NA')
    
    # FIRST NAME
    cdict['first_name'] = [poc[i].split()[-2] for i in range(len(poc))]
    
    # PHONE
    cdict['phone'] = [contact_info[i].split('\n')[1] for i in range(len(companies))]
    
    return cdict