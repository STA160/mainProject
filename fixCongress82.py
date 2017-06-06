#!/usr/bin/env python2

import pandas as pd
import sys

# Run: python fixCcongress82.py [Name of csv file]
# This script handles the mistake in the csv files where some rows have a congress equal to 82 
# This occurs for some dates with years 2016 and 2017

# Read in the data:
tfDiff = pd.read_csv(sys.argv[1], parse_dates = ["date"])

# If no year column, add one:
try:
	tfDiff["Year"]
except:
	tfDiffYear['Year'] = [timestamp.year for timestamp in tfDiffYear.date]
	tfDiffYear['Month'] = [timestamp.month for timestamp in tfDiffYear.date]

# Year 2017 belongs in congress 115:
tfDiff.loc[(tfDiff.congress == 82) & (tfDiff.Year == 2017), "congress"] = 115

# Year 2016 belongs in congress 114:
tfDiff.loc[(tfDiff.congress == 82) & (tfDiff.Year == 2016), "congress" ] = 114

# Save to same csv name:
tfDiff.to_csv(sys.argv[1])
print "You can find your csv in the cwd folder with the name " + sys.argv[1]
