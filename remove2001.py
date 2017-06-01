#!/usr/bin/env 

import pandas as pd
import sys

def main():
	"""
	This script takes in the congressional records csv file and removes any data with the year 2001. 
	This somehow happened along the way even though our data should only have years 2006 and on. 
	"""
	cong = pd.read_csv(sys.argv[1], parse_dates = ["date"])
	cong = cong[cong["date"].dt.year != 2001] # Removes about 1400 instances
	
	cong.to_csv("congressionalRecords.csv")


if __name__ == '__main__':  main()

