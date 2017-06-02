import pandas as pd
from collections import Counter
import numpy as np
import nltk
from nltk.corpus import stopwords

import csv
import itertools
import operator
import numpy as np
import nltk
import sys
from datetime import datetime
from utils import *
import re

#filepath1 = "C:\Users\Graham\Documents\STA 160\\tfidfparty2017.csv"
#filepath2 = "~\Documents\STA 160\congressional record\congressionalRecords.csv"

def tfidfDiffs(filepath1, filepath2):

"""
***WARNING***
THIS SCRIPT TAKES ABOUT 10 MINUTES TO RUN PER RECORD RIGHT NOW
*************

Input: filepath1 = tfidf csv
	   filepath1 = congressional record csv
Output: congressional record with mean tfidf difference scores for each text chunk
		added as a column 
"""
	
	dat = pd.read_csv(filepath1)

	dat = dat[dat['idf']>0]
	dat = dat[dat['party'].isin(['Republican', 'Democrat'])]

	repwords = dat[dat['party']=='Republican']
	demwords = dat[dat['party']=='Democrat']

	words = pd.merge(repwords, demwords, on='word', how='outer')

	tfidf = t.drop(['Unnamed: 0_x', 'party_x','n_x', 'tf_x', 'idf_x', 'Unnamed: 0_y', 'party_y','n_y', 'tf_y', 'idf_y'], axis=1)
	tfidf.columns = ['word', 'tfidf_r', 'tfidf_d']

	diff = [b.loc[x]['tfidf_r'] - b.loc[x]['tfidf_d'] for x in range(len(b))]
	tfidf['diff'] = diff

	data = pd.read_csv(filepath2)
	text = [re.split(' ', x) for x in data['text']]

	diffs = []
	for i in range(len(text)):
		df = pd.DataFrame(text[i])
		df.columns = ['word']
		y = tfidf.merge(df)['diff']
		diffs.append(np.mean(y))

	data['tfidfd'] = diffs

	return rep_record

def main():
	# Call the function and have the script save a csv:  
	tfidfDiffs(sys.argv[1], sys.argv[2]).to_csv('cong_record_tfidfDiff.csv')
	print "You can find your csv in the cwd folder with the name cong_record_tfidfDiff.csv"
	
if __name__ == "__main__": main()

