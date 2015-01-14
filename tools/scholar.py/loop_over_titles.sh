#!/bin/bash
while read p; do
    ./scholar.py -c 1 -p "$p" --citation=bt >> refs.bib
done < paper_titles.txt
