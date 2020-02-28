#!/bin/bash

# take a CSV file

# remove the header

# extract columns 2-6 that are delimited by $3 (insert delimiter as third argument)

# substitute semicolon delimiter for spaces

# sort in reverse, numerically, by the body mass

# redirect to a csv file

tail -n +2 $1 | cut -d $3 -f 2-6 | tr $3 " " | sort -r -n -k 6 > $2
