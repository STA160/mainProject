#Party Bias Clustering of US Legislators
 
Our project focuses on analyzing the language used by US legislators. 
We want to know how their language varies by party and state. 
We also want to know how their language changes over time.

Scripts are used roughly in the following order:

1. congressPdfPuller.pl	congress pdf massive downloader -Randy
2. congTextToCSV.py	Imports function from updated parsing file
     READMEtextToCSV.txt	Fixed small typo
3. listCongressNumberAndFilenameInCSV.pl	just a helper tool to extract distinct congress number and date
4. remove2001.py	Removes 2001 dates from congressionalRecords.csv
5. c_processor_final.py	Catches files with harder text to decode
     legislators-current.json.txt	removed parallel delta tf-idf script and appended original.
     legislators-historical.json.txt	removed parallel delta tf-idf script and appended original.
6. splitCsvByDate.pl	changed split script to output csvs, and started working on markup
7. {tfidf calculation in tf_idf folder}
8. tfidfDiffs.py	removed parallel delta tf-idf script and appended original.
9. allYearsTFIDF_Diff.py	Add normalized delta tfidf column
10. fixCongress82.py	Fixes mistake where congress = 82
11. parallel_script.sh	added extra formatting to fix the filenames
12. gnuParallelList.txt	removed parallel delta tf-idf script and appended original.
13. cleanedTableData.html	added html table parser and html file to get approval disapproval scores
14. htmlTableParser.pl	took percent stuff off
