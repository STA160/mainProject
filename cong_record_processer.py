
# coding: utf-8

# In[504]:

import sys
import pandas as pd
import os
import re
from collections import Counter
import string
from textblob import TextBlob
import json
from dateutil import parser


# In[472]:

#with open (sys.argv[1], "r") as myfile: data = myfile.read().replace('\n', '')
with open ('C:\\Users\\Graham\\Documents\\STA 160\\congressional record\\CREC-2017-04-24.txt', "r") as myfile:
    data = myfile.read().replace('\n', ' ')


# In[573]:

#FIND ALL THE NAMES
names = re.findall('[M][s|r][\.][\s][A-Z]{2,}', data)
names = [re.sub('[M][s|r][\.][\s]', '', x) for x in names]


# In[574]:

#FIND ASSOCIATED TEXT FOR EACH NAME
split = re.split('[M][s|r][\.][\s][A-Z]{2,}', data)
split = split[1:]


# In[575]:

#GET THE DATE OF THE RECORD
date = re.findall('(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[\s][0-9]{1,2}[\,][\s][0-9]{4}'
           ,data)[0]
date = parser.parse(date)
date = [date]*len(names)


# In[576]:

record = pd.DataFrame({'text': split,'names': names, 'date': date})


# In[577]:

#REMOVE UNICODE
record['text'] = [s.decode('unicode_escape').encode('ascii','ignore') for s in record['text']]


# In[578]:

#REMOVE PUNCTUATION
record['text'] = [r.translate(None, string.punctuation) for r in record['text']]


# In[579]:

#REMOVE NUMBERS
record['text'] = [re.sub(r'\d+', '', x) for x in record['text']]


# In[580]:

#REMOVE NON-SPEECH BEURECRATIC CODES
record['text'] = [re.sub(r'[A-Z]{2,}', '', x) for x in record['text']]


# In[581]:

#REMOVE EXCESS SPACES
record['text'] = [re.sub(r'[[:space]]{2,}', ' ', x) for x in record['text']]


# In[582]:

#REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
remove = [len(x)<=30 for x in record['text']]
record['remove'] = remove
record = record.drop(record[record.remove==True].index)
record = record.drop(['remove'], axis=1)


# In[394]:

#LOAD CURRENT LEGISLATOR INFORMATION
with open ('C:\\Users\\Graham\\Documents\\STA 160\\legislators-current.json', "r") as myfile:
    current_legislators = json.load(myfile)


# In[556]:

#FIND PARTY
party = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['party'] for x in range(len(current_legislators))]


# In[559]:

#FIND STATE
state = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['state'] for x in range(len(current_legislators))]


# In[564]:

#FIND NAMES
lnames = [current_legislators[x]['name']['last'].upper() for x in range(len(current_legislators))]


# In[585]:

leg_data = pd.DataFrame({'party': party,'state': state, 'names': lnames})


# In[588]:

congressional_record = record.merge(leg_data,on='names')

