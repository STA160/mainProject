import sys
import pandas as pd
import re
import string
import json
from dateutil import parser

with open (sys.argv[1], 'r') as myfile:
    data = myfile.read().replace('\n', ' ')

def parseRecord(data):
    names = re.findall('[M][s|r][\.][\s][A-Z]{2,}', data)
    names = [re.sub('[M][s|r][\.][\s]', '', x) for x in names]
    split = re.split('[M][s|r][\.][\s][A-Z]{2,}', data)
    split = split[1:]
    #GET THE DATE OF THE RECORD
    date = re.findall('(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[\s][0-9]{1,2}[\,][\s][0-9]{4}'
           ,data)[0]
    date = parser.parse(date)
    date = [date]*len(names)
    record = pd.DataFrame({'text': split,'names': names, 'date': date})
    #REMOVE UNICODE
    record['text'] = [s.decode('unicode_escape').encode('ascii','ignore') for s in record['text']]
    #REMOVE PUNCTUATION
    record['text'] = [r.translate(None, string.punctuation) for r in record['text']]
    #REMOVE NUMBERS
    record['text'] = [re.sub(r'\d+', '', x) for x in record['text']]
    #REMOVE NON-SPEECH BEURECRATIC CODES
    record['text'] = [re.sub(r'[A-Z]{2,}', '', x) for x in record['text']]
    #REMOVE EXCESS SPACES
    record['text'] = [re.sub(r'[[:space]]{2,}', ' ', x) for x in record['text']]
    #REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
    remove = [len(x)<=30 for x in record['text']]
    record['remove'] = remove
    record = record.drop(record[record.remove==True].index)
    record = record.drop(['remove'], axis=1)
    #LOAD CURRENT LEGISLATOR INFORMATION
    with open ('C:\\Users\\Graham\\Documents\\STA 160\\legislators-current.json', "r") as myfile:
        current_legislators = json.load(myfile)
    #FIND PARTY
    party = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['party'] for x in range(len(current_legislators))]
    #FIND STATE
    state = [current_legislators[x]['terms'][len(current_legislators[x]['terms'])-1]['state'] for x in range(len(current_legislators))]
    #FIND NAMES
    lnames = [current_legislators[x]['name']['last'].upper() for x in range(len(current_legislators))]
    leg_data = pd.DataFrame({'party': party,'state': state, 'names': lnames})
    congressional_record = record.merge(leg_data,on='names')

    return(congressional_record)
