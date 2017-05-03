
# In[245]:

import sys
import pandas as pd
import os
import re
from collections import Counter
import string
from textblob import TextBlob
import nltk


# In[187]:

#with open (sys.argv[1], "r") as myfile: data = myfile.read().replace('\n', '')
with open ('C:\\Users\\Graham\\Documents\\STA 160\\congressional record\\CREC-2017-04-24.txt', "r") as myfile:
    data = myfile.read().replace('\n', '')


# In[188]:

#FIND ALL THE NAMES
names = re.findall('[M][s|r][\.][\s][A-Z]{2,}', data)


# In[298]:

#FIND ASSOCIATED TEXT FOR EACH NAME
split = re.split('[M][s|r][\.][\s][A-Z]{2,}', data)


# In[299]:

record = pd.DataFrame({'text': split,'names': names})


# In[265]:

#REMOVE UNICODE
record['text'] = [s.decode('unicode_escape').encode('ascii','ignore') for s in record['text']]


# In[266]:

#REMOVE PUNCTUATION
record['text'] = [r.translate(None, string.punctuation) for r in record['text']]


# In[274]:

#REMOVE NUMBERS
record['text'] = [re.sub(r'\d+', '', x) for x in record['text']]


# In[279]:

#REMOVE NON-SPEECH BEURECRATIC CODES
record['text'] = [re.sub(r'[A-Z]{2,}', '', x) for x in record['text']]


# In[282]:

#REMOVE EXCESS SPACES
record['text'] = [re.sub(r'[[:space]]{2,}', ' ', x) for x in record['text']]


# In[285]:

#REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
to_drop = [len(x)<=30 for x in record['text']]


# In[292]:

record = pd.DataFrame({'text': split,'names': names, 'remove': to_drop})


# In[ ]:

record = record.drop(record[record.remove==True].index)


# In[284]:

record = record.drop(['remove'], axis=1)
