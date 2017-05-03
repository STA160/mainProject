

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

with open (sys.argv[1], "r") as myfile: data = myfile.read().replace('\n', '')

# In[188]:

names = re.findall('[M][s|r][\.][\s][A-Z]{2,}', data)

# In[189]:

split = re.split('[M][s|r][\.][\s][A-Z]{2,}', data)[0:len(names)]


# In[190]:

cong_record = pd.DataFrame({'text': split,'names': names})


# In[191]:

#REMOVE STRINGS THAT ARE OBVIOUSLY TOO SHORT
to_drop = [len(cong_record['text'][x])<=30 for x in range(len(cong_record))]


# In[192]:

cong_record = pd.DataFrame({'text': split,'names': names, 'remove': to_drop})


# In[193]:

cong_record = cong_record.drop(cong_record[cong_record.remove==True].index)


# In[202]:

record = cong_record.drop(['remove'], axis=1)


# In[242]:

#REMOVE PUNCTUATION
record['text'] = [r.translate(None, string.punctuation) for r in record['text']]

print(record)
