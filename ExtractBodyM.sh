#!/bin/bash

# take a CSV file

# remove the header

# extract columns 2-6 that are delimited by ";"

# substitute semicolon delimiter for spaces

# sort in reverse, numerically, by the body mass

# redirect to a csv file

tail -n +2 $1 | cut -d ";" -f 2-6 | tr ";" " " | sort -r -n -k 6 > $2
