#!/usr/bin/env 

import pandas as pd
import sys
from collections import Counter
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+') # This one removes punctuation

# Goes through the csv and adds a word count column for the count of words in that text
# This data is needed for WordCountPlotsTableau

def main():
	# Read in the csv:
	cong = pd.read_csv(sys.argv[1], parse_dates = ["date"])
	
	# Just want the two parties:
	cong = cong[cong["party"].isin(["Republican", "Democrat"])]

	# Add a wordCount column that counts the words in each text chunk:
	AddCounts = pd.DataFrame.from_dict({"WordCount": [len(tokenizer.tokenize((row["text"].lower()))) for index, row in cong.iterrows()], 
										'Unnamed: 0': [index for index, row in cong.iterrows()]   })	
	cong = pd.merge(cong, AddCounts, on = "Unnamed: 0", how = "left")
	
	# Drop that unnamed column:
	cong = cong.drop('Unnamed: 0', 1)
	
	# Add the columns year and month:
	cong['Year'] = [timestamp.year for timestamp in cong.date]
	cong['Month'] = [timestamp.month for timestamp in cong.date]
	
	# Save that csv:
	cong.to_csv("congRecordsMore.csv")
	print "You can find your csv in the cwd folder with the name congRecordsMore.csv"
	
if __name__ == '__main__':  main()
