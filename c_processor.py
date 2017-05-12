
# coding: utf-8

# In[37]:

import sys
import pandas as pd
import re
import string
import json
from dateutil import parser
import requests as requests
from bs4 import BeautifulSoup


# In[ ]:

def decodeText(text):
    """
    Input: A chunk of text. 
    Output: The encoded version of that chunk. 
    """
    try:  
        return text.decode('unicode_escape').encode('ascii','ignore')
    except: # Special case where trouble encoding "\\" - file 2015-11-16
        text = "".join([t + '\\\\' for t in text.split('\\')])
        return text.decode('unicode_escape').encode('ascii','ignore')


# In[2]:

#with open (sys.argv[1], "r") as myfile: data = myfile.read().replace('\n', '')
with open ('C:\\Users\\Graham\\Documents\\STA 160\\congressional record\\CREC-2017-04-05.txt', "r") as myfile:
    data = myfile.read().replace('\n', ' ')


# In[3]:

#FIND ALL THE NAMES
names = re.findall('[M][s|r][\.][\s][A-Z]{2,}', data)
names = [re.sub('[M][s|r][\.][\s]', '', x) for x in names]


# In[4]:

#FIND ASSOCIATED TEXT FOR EACH NAME
split = re.split('[M][s|r][\.][\s][A-Z]{2,}', data)
split = split[1:]


# In[5]:

#GET THE DATE OF THE RECORD
date = re.findall('(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[\s][0-9]{1,2}[\,][\s][0-9]{4}'
           ,data)[0]
date = parser.parse(date)
date = [date]*len(names)


# In[6]:

#GET WHICH CONGRESS IT IS
congress = re.findall('[0-9]{3}[\s](?:th)', data)[0]
congress = [congress]*len(names)
congress = [x[0:3] for x in congress]


# In[7]:

record = pd.DataFrame({'text': split,'names': names, 'date': date, 'congress': congress})


# In[8]:

#REMOVE UNICODE
record['text'] = [s.decode('unicode_escape').encode('ascii','ignore') for s in record['text']]


# In[9]:

#REMOVE PUNCTUATION
record['text'] = [r.translate(None, string.punctuation) for r in record['text']]


# In[10]:

#REMOVE NUMBERS
record['text'] = [re.sub(r'\d+', '', x) for x in record['text']]


# In[11]:

#REMOVE NON-SPEECH BEURECRATIC CODES
record['text'] = [re.sub(r'[A-Z]{2,}', '', x) for x in record['text']]


# In[12]:

#REMOVE EXCESS SPACES
record['text'] = [re.sub(r'[[:space]]{2,}', ' ', x) for x in record['text']]


# In[13]:

#REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
remove = [len(x)<=30 for x in record['text']]
record['remove'] = remove
record = record.drop(record[record.remove==True].index)
record = record.drop(['remove'], axis=1)


# In[87]:

#LOAD CURRENT LEGISLATOR INFORMATION
#with open (sys.argv[2], "r") as myfile: current_legislators = json.load(myfile)
with open ('C:\\Users\\Graham\\Documents\\STA 160\\legislators-current.json', "r") as myfile:
    cl = json.load(myfile)


# In[88]:

#FIND PARTY
party = [cl[x]['terms'][len(cl[x]['terms'])-1]['party'] for x in range(len(cl))]


# In[89]:

#FIND STATE
state = [cl[x]['terms'][len(cl[x]['terms'])-1]['state'] for x in range(len(cl))]


# In[90]:

#FIND NAMES
lnames = [cl[x]['name']['last'].upper() for x in range(len(cl))]


# In[91]:

start_year = [cl[x]['terms'][0]['start'][0:4] for x in range(len(cl))]


# In[92]:

leg_data = pd.DataFrame({'party': party,'state': state, 'names': lnames, 'start_year': start_year})


# In[94]:

leg_data = leg_data.drop_duplicates(subset=['names'], keep='first')


# In[135]:

#LOAD PAST LEGISLATOR INFORMATION
#with open (sys.argv[3], "r") as myfile: lh = json.load(myfile)
with open ('C:\\Users\\Graham\\Documents\\STA 160\\legislators-historical.json', "r") as myfile:
    lh = json.load(myfile)


# In[136]:

lh=[x for x in lh if int(x['terms'][0]['end'][0:4])>=2006]


# In[137]:

party = []
for i in range(len(lh)):
    try: party = party + [lh[i]['terms'][0]['party']]
    except:
        party = party + ['NA']   


# In[138]:

names = [x['name']['last'].upper() for x in lh]


# In[139]:

state = [x['terms'][0]['state'] for x in lh]


# In[140]:

end_year = [x['terms'][len(x['terms'])-1]['end'][0:4] for x in lh]


# In[141]:

start_year = [x['terms'][0]['start'][0:4] for x in lh]


# In[147]:

hleg_data = pd.DataFrame({'party': party, 'names': names, 'state': state, 'end_year': end_year, 'start_year': start_year})


# In[148]:

ld = leg_data.append(hleg_data)


# In[155]:

ld = ld.drop_duplicates(subset=['names'], keep='first')


# In[164]:




# In[161]:

c_record = record.merge(ld, on='names', how='left')


# In[119]:

c_record.groupby(c_record['names'].tolist()).size().reset_index().rename(columns={0:'count'})


# In[39]:

url = 'https://www.senate.gov/reference/Sessions/sessionDates.htm'
a = requests.get(url)
r = a.text
soup = BeautifulSoup(r, 'html.parser')


# In[ ]:

congress = re.findall('[0-9]{3}[\s](?:th)', data)[0]


# In[206]:

congressional_record.to_csv('congressional_record_' + str(congressional_record['date'][0])[0:10] + '.csv')

