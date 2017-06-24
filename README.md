#Party Bias Clustering of US Legislators
 
Our project focuses on analyzing the language used by US legislators. 
We want to know how their language varies by party and state. 
We also want to know how their language changes over time.

Scripts are used roughly in the following order:

1. congressPdfPuller.pl	| congress pdf massive downloader
2. congTextToCSV.py	| Imports function from updated parsing file
     READMEtextToCSV.txt
3. listCongressNumberAndFilenameInCSV.pl	| just a helper tool to extract distinct congress number and date
4. remove2001.py	| Removes 2001 dates from congressionalRecords.csv since we're only interested in 2006+
5. c_processor_final.py	| Preprocessor to parse congressional record PDF's into CSV's
     legislators-current.json.txt	| biographical information for current legislators
     legislators-historical.json.txt	| biographical information for past legislators
6. splitCsvByDate.pl	| splits processed CSV's by date
7. {tfidf calculation in tf_idf folder}
8. tfidfDiffs.py	| calculates Delta TF-IDF's
9. allYearsTFIDF_Diff.py	| runs the tfidfDiffs.py script over all the congressional records
10. fixCongress82.py	| Fixes mistake where congress = 82
11. parallel_script.sh	| added extra formatting to fix some errors in filenames
12. gnuParallelList.txt	| removed parallel delta tf-idf script and appended original.
13. cleanedTableData.html	| added html table parser and html file to get approval disapproval scores
14. htmlTableParser.pl	| took percent stuff off
