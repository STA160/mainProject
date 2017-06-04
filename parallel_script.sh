cat gnuParallelList.txt | parallel --colsep ' ' python tfidfDiffsParallelMod.py {1} {2}
