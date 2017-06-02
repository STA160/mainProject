import pandas as pd
import numpy as np
import csv
import itertools
import operator
import sys
import re

#filepath1 = "C:\Users\Graham\Documents\STA 160\\tfidfparty2017.csv"
#filepath2 = "~\Documents\STA 160\congressional record\congressionalRecordsSmall.csv"

def tfidfDiffs(filepath1, filepath2):

	"""
	Input: filepath1 = tfidf csv
		   filepath1 = congressional record csv
	Output: congressional record with mean tfidf difference scores for each text chunk
			added as a column 
	"""
	
	#LOAD IN TFIDF FILE AND GET WORDS THAT HAVE A NONZERO SIGNIFICANCE
	dat = pd.read_csv(filepath1)
	dat = dat[dat['idf']>0]
	dat = dat[dat['party'].isin(['Republican', 'Democrat'])]

	#SPLIT WORDS BY PARTY
	repwords = dat[dat['party']=='Republican']
	demwords = dat[dat['party']=='Democrat']
	words = pd.merge(repwords, demwords, on='word', how='outer')

	#DROP UNNESSESARY COLUMNS
	tfidf = words.drop(['Unnamed: 0_x', 'party_x','n_x', 'tf_x', 'idf_x', 'Unnamed: 0_y', 'party_y','n_y', 'tf_y', 'idf_y'], axis=1)
	tfidf.columns = ['word', 'tfidf_r', 'tfidf_d']

	#FIND THE DELTA(TFIDF) BETWEEN REPUBLICAN AND DEMOCRAT FOR EVERY WORD
	diff = [tfidf.loc[x]['tfidf_r'] - tfidf.loc[x]['tfidf_d'] for x in range(len(tfidf))]
	tfidf['diff'] = diff

	#LOAD THE CONGRESSIONAL FILE
	data = pd.read_csv(filepath2)
	
	#SPLIT EACH WORD CHUNK SO WE HAVE A LIST OF LISTS. MERGE THE WORDS IN EACH WORD CHUNK
	#WITH ITS DELTA(TFIDF) SCORE
	text = [(re.split(' ', x.lower())) for x in data['text']]
	diffs = []
	for i in range(len(text)):
		df = pd.DataFrame(text[i])
		df.columns = ['word']
		y = tfidf.merge(df)['diff']
		diffs.append(np.mean(y))

	data['tfidfd'] = diffs

	return data

def main():
	# Call the function and have the script save a csv:  
	tfidfDiffs(sys.argv[1], sys.argv[2]).to_csv('cong_record_tfidfDiff.csv')
	print "You can find your csv in the cwd folder with the name cong_record_tfidfDiff.csv"
	
if __name__ == "__main__": main()

