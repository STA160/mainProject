#!/usr/bin/env 

import pandas as pd
import os

def main():
	"""
	Run this script in the folder outside of delta_tfidf.
	It takes all of the csvs, combines them into one csv, and adds two columns: Year and Month.
	This makes plotting a little easier. 
	"""
	tfDiff = pd.DataFrame()
	
	# For each tfidf diff csv file:
	for f in os.listdir("./delta_tfidf"):
		
		# Read it in and parse the dates:
		tfDiffYear = pd.read_csv("delta_tfidf/" + f, parse_dates = ["date"])
    
		# Add Year and Month:
		tfDiffYear['Year'] = [timestamp.year for timestamp in tfDiffYear.date]
		tfDiffYear['Month'] = [timestamp.month for timestamp in tfDiffYear.date]
    
		# Combine each year:
		tfDiff = tfDiff.append(tfDiffYear)
		
	# Normalize tfidf diffs:
	minDiff = min(tfDiff['tfidfd'])
	maxDiff = max(tfDiff['tfidfd'])
	tfDiff['tfidf_norm'] = [2*((x - minDiff)/(maxDiff - minDiff)) - 1 for x in tfDiff['tfidfd']]		
	
	# Save to a csv:
	tfDiff.to_csv("allYearsTFIDF_Diff.csv")
	print "You can find your csv in the cwd folder with the name allYearsTFIDF_Diff.csv"
	
if __name__ == '__main__':  main()
    
