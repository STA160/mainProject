#!/bin/sh
#this script runs gnu parallel to use the delta tf-idf script in parallel so it doesn't take a day to finish. The more cores the better. also mmore memory is better too

echo "converting all tf idf filename spaces to underscores for unix sakes"

mv "2006 TF_IDF_PARTY.TXT" 2006_TF_IDF_PARTY.TXT 
mv "2007 TF_IDF_PARTY.TXT" 2007_TF_IDF_PARTY.TXT 
mv "2008 TF_IDF_PARTY.TXT" 2008_TF_IDF_PARTY.TXT 
mv "2009 TF_IDF_PARTY.TXT" 2009_TF_IDF_PARTY.TXT 
mv "2010 TF_IDF_PARTY.TXT" 2010_TF_IDF_PARTY.TXT 
mv "2011 TF_IDF_PARTY.TXT" 2011_TF_IDF_PARTY.TXT 
mv "2012 TF_IDF_PARTY.TXT" 2012_TF_IDF_PARTY.TXT 
mv "2013 TF_IDF_PARTY.TXT" 2013_TF_IDF_PARTY.TXT 
mv "2014 TF_IDF_PARTY.TXT" 2014_TF_IDF_PARTY.TXT 
mv "2015 TF_IDF_PARTY.TXT" 2015_TF_IDF_PARTY.TXT 
mv "2016 TF_IDF_PARTY.TXT" 2016_TF_IDF_PARTY.TXT 
mv "2017 TF_IDF_PARTY.TXT" 2017_TF_IDF_PARTY.TXT 

cat gnuParallelList.txt | parallel --colsep ' ' python tfidfDiffs.py {1} {2}
