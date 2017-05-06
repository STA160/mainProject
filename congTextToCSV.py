#!/usr/bin/env python2

from cong_record_processer import cr_processer
from cong_record_processer import decodeText
import sys
import os
import pandas as pd
import re
import string
import json
from dateutil import parser

def main(pathToFolder, pathToCurrLeg, pathToHistLeg):
	"""
	Input:
		pathToFolder = The file path to the folder containing the congress text files.
		pathToCurrLeg = The file path to the file called legislators-current.json.txt.
		pathToHistLeg = The path to the file called legislators-historical.json.txt.
	Output:
		A csv file called congressRecords.csv with rows from all of the text files in the specified folder 
		and columns "congress", "date", "names", "text", "party_x", "state_x", "party_y", and "state_y"
	"""

	# Create empty dataframe to append to later:
	DF = pd.DataFrame(columns = ["congress", "date", "names", "text", "party_x", "state_x", "party_y", "state_y"])

	# For every file in the folder:
	for filePath in [pathToFolder + "/" + f for f in os.listdir(pathToFolder) if f != "pdflist.txt"]:
		
		# Send to the parsing function that returns a DataFrame:
		newDF = cr_processer(filePath, pathToCurrLeg, pathToHistLeg)
		
		# Keep appending to the DataFrame:
		DF = DF.append(newDF)		
		
	# Save to csv:	
	DF.to_csv("congressionalRecords.csv")
	print "You can find your csv in the cwd folder with the name congressionalRecords.csv"
	
	
if __name__ == "__main__": main(sys.argv[1], sys.argv[2], sys.argv[3])


    
    
