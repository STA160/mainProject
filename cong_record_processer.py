
# coding: utf-8

# In[161]:

import sys
import pandas as pd
import re
import string
import json
from dateutil import parser


# In[162]:
def cr_processer(sys.argv[1]):

   """
   INPUT: filepath to a .txt file of the daily Congressional Record put out by the US Congress
   OUTPUT: .csv of the parsed data, containing congress#, date, what was said and the last names,
   party affiliation, and state of who said it. Note that all legislators with duplicate last names
   have been remove for ease of analysis
   """
    
    #IF SYS.ARGV[1] DOESN'T WORK, USE 'FILEPATH' INSTEAD
    with open (sys.argv[1], "r") as myfile: data = myfile.read().replace('\n', '')
    
    # In[163]:
    
    #FIND ALL THE NAMES
    names = re.findall('[M][s|r][\.][\s][A-Z]{2,}', data)
    names = [re.sub('[M][s|r][\.][\s]', '', x) for x in names]
    
    
    # In[164]:
    
    #FIND ASSOCIATED TEXT FOR EACH NAME
    split = re.split('[M][s|r][\.][\s][A-Z]{2,}', data)
    split = split[1:]
    
    
    # In[165]:
    
    #GET THE DATE OF THE RECORD
    date = re.findall('(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[\s][0-9]{1,2}[\,][\s][0-9]{4}'
               ,data)[0]
    date = parser.parse(date)
    date = [date]*len(names)
    
    
    # In[166]:
    
    #GET WHICH CONGRESS IT IS
    congress = re.findall('[0-9]{3}[\s](?:th)', data)[0]
    congress = [congress]*len(names)
    congress = [x[0:3] for x in congress]
    
    
    # In[167]:
    
    record = pd.DataFrame({'text': split,'names': names, 'date': date, 'congress': congress})
    
    
    # In[168]:
    
    #REMOVE UNICODE
    record['text'] = [s.decode('unicode_escape').encode('ascii','ignore') for s in record['text']]
    
    
    # In[169]:
    
    #REMOVE PUNCTUATION
    record['text'] = [r.translate(None, string.punctuation) for r in record['text']]
    
    
    # In[170]:
    
    #REMOVE NUMBERS
    record['text'] = [re.sub(r'\d+', '', x) for x in record['text']]
    
    
    # In[171]:
    
    #REMOVE NON-SPEECH BEURECRATIC CODES
    record['text'] = [re.sub(r'[A-Z]{2,}', '', x) for x in record['text']]
    
    
    # In[172]:
    
    #REMOVE EXCESS SPACES
    record['text'] = [re.sub(r'[[:space]]{2,}', ' ', x) for x in record['text']]
    
    
    # In[173]:
    
    #REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
    remove = [len(x)<=30 for x in record['text']]
    record['remove'] = remove
    record = record.drop(record[record.remove==True].index)
    record = record.drop(['remove'], axis=1)
    
    
    # In[174]:
    
    #LOAD CURRENT LEGISLATOR INFORMATION
    with open ('C:\\Users\\Graham\\Documents\\STA 160\\legislators-current.json', "r") as myfile:
        current_legislators = json.load(myfile)
    
    
    # In[175]:
    
    #FIND PARTY
    party = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['party'] for x in range(len(current_legislators))]
    
    
    # In[176]:
    
    #FIND STATE
    state = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['state'] for x in range(len(current_legislators))]
    
    
    # In[177]:
    
    #FIND NAMES
    lnames = [current_legislators[x]['name']['last'].upper() for x in range(len(current_legislators))]
    
    
    # In[178]:
    
    leg_data = pd.DataFrame({'party': party,'state': state, 'names': lnames})
    
    
    # In[179]:
    
    leg_data = leg_data.drop_duplicates(subset=['names'], keep='first')
    
    
    # In[180]:
    
    congressional_record = record.merge(leg_data,on='names')
    
    
    # In[183]:
    
    #LOAD PAST LEGISLATOR INFORMATION
    with open ('C:\\Users\\Graham\\Documents\\STA 160\\legislators-historical.json', "r") as myfile:
        lh = json.load(myfile)
    
    
    # In[184]:
    
    party = []
    for i in range(len(lh)):
        try: party = party + [lh[i]['terms'][0]['party']]
        except:
            party = party + ['NA']   
    
    
    # In[185]:
    
    names = [x['name']['last'].upper() for x in lh]
    
    
    # In[186]:
    
    state = [x['terms'][0]['state'] for x in lh]
    
    
    # In[187]:
    
    hleg_data = pd.DataFrame({'party': party, 'names': names, 'state': state})
    
    
    # In[188]:
    
    hleg_data = hleg_data.drop_duplicates(subset=['names'], keep='first')
    
    
    # In[190]:
    
    congressional_record = congressional_record.merge(hleg_data,on='names')
    
    
    # In[194]:
    
    return(congressional_record.to_csv('congressional_record.csv'))
    
