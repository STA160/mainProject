#!/bin/sh
cat gnuParallelList.txt | parallel --colsep ' ' python tfidfDiffs.py {1} {2}
