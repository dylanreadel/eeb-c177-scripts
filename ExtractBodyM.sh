#!/bin/bash

# take the CSV file Pacifici2013_data.csv

# remove the header

# extract columns 2-6 that are delimited by ";"

# substitute semicolon delimiter for spaces

# sort in reverse, numerically, by the body mass

# redirect to a body mass csv file

tail -n +2 ~/Developer/repos/CSB/unix/data/Pacifici2013_data.csv | cut -d ";" -f 2-6 | tr ";" " " | sort -r -n -k 6 > BodyM.csv
