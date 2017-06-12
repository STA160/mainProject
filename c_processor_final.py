
# coding: utf-8

# In[37]:

import sys
import pandas as pd
import re
import string
import json
from dateutil import parser


# In[1]:

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

def cr_processer(filePath1, filePath2, filePath3):

    """
    INPUT: three filepaths 
    1. to a .txt file of the daily Congressional Record put out by the US Congress. 
    2. path to legislators-current.json.txt - get from google drive
    3. path to legislators-historical.json.txt - get from google drive
    OUTPUT: dataframe of the parsed data, containing congress#, date, what was said and the last names,
    party affiliation, and state of who said it. Note that all legislators with duplicate last names
    have been remove for ease of analysis
    """
        
    #IF SYS.ARGV[1] DOESN'T WORK, USE 'FILEPATH' INSTEAD
    with open (filePath1, "r") as myfile: data = myfile.read().replace('\n', '')


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
    congress = re.findall('[0-9]{3}', data)[0]
    congress = [congress]*len(names)
    congress = [x[0:3] for x in congress]
    
# In[7]:

    record = pd.DataFrame({'text': split,'names': names, 'date': date, 'congress': congress})


# In[8]:

    #REMOVE UNICODE
    record['text'] = [decodeText(s) for s in record['text']]

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
    record['text'] = [' '.join(word for word in x.split() if len(word)>3) for x  in record['text']]
    

# In[13]:

    #REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
    remove = [len(x)<=30 for x in record['text']]
    record['remove'] = remove
    record = record.drop(record[record.remove==True].index)
    record = record.drop(['remove'], axis=1)


# In[87]:

    #LOAD CURRENT LEGISLATOR INFORMATION
    with open (filePath2, "r") as myfile:
        current_legislators = json.load(myfile)
    
    # In[88]:
    
    #FIND PARTY
    party = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['party'] for x in range(len(current_legislators))]
    
    
    # In[89]:
    
    #FIND STATE
    state = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['state'] for x in range(len(current_legislators))]
    
    
    # In[90]:
    
    #FIND NAMES
    lnames = [current_legislators[x]['name']['last'].upper() for x in range(len(current_legislators))]
    
    
    # In[91]:
    
    start_year = [current_legislators[x]['terms'][0]['start'][0:4] for x in range(len(current_legislators))]
    
    
    # In[92]:
    
    leg_data = pd.DataFrame({'party': party,'state': state, 'names': lnames, 'start_year': start_year})
    
    
    # In[94]:
    
    leg_data = leg_data.drop_duplicates(subset=['names'], keep='first')
    
    
    # In[135]:
    
    #LOAD PAST LEGISLATOR INFORMATION
    with open (filePath3, "r") as myfile:
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
    
    
    # In[161]:
    
    c_record = record.merge(ld, on='names', how='left')

    return(c_record)
    
def main():
	# Call the function and have the script save a csv:  
	cr_processer(sys.argv[1], sys.argv[2], sys.argv[3]).to_csv('congressional_record.csv')
	print "You can find your csv in the cwd folder with the name congressional_record.csv"
	
if __name__ == "__main__": main()

