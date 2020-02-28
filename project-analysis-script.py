#!/usr/bin/env python

import pandas
import pandas as pd
import datetime
import numpy
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import os

def visualize_occurrences_by_season():

    inputfile = ''
    inputfile = input('Enter the dataset filename: ')

    assert len(inputfile) != 0, 'No filename entered.'
    assert type(inputfile) == str, 'Filename is not a string: %r' % inputfile

    print('Analyzing data...')

    # read in the csv data file of species observations
    data = pd.read_csv(inputfile)

    date_col = ''
    date_col = input('Enter the observation date column header name: ')
    if date_col in data.columns:
        print('Column found!')
    assert date_col in data.columns, 'Date column header not found!'

    # extract the dates column to a list
    dates = data[date_col].to_list()

    # create an empty list for dates that are separated using datetime
    dates_separated = list()

    # iterate through dates to separate them using datetime
    for i in dates:
        dates_separated.append(datetime.strptime(i, "%Y-%m-%d"))

    # create an empty list for observations by month
    months = list()

    # iterate through separated dates list to extract just the month as an integer
    for m in dates_separated:
        months.append(m.month)

    # create an empty list for observations by season
    observations_by_season = list()

    # iterate through each observation in the months list
    # by using an if statement for each season
    # if the month is in the season's numerical range
    # the season is appended to the observation_by_season list
    for x in months:
        if x in range(1, 4):
            observations_by_season.append('Winter')
        if x in range(4, 7):
            observations_by_season.append('Spring')
        if x in range(7, 10):
            observations_by_season.append('Summer')
        if x in range (10, 13):
            observations_by_season.append('Autumn')

    # create an empty default dictionary with integers
    # for the count of each observation by season
    season_counts = defaultdict(int)

    # iterate through seasons in observations_by_season list
    # add a count for each season to the season_counts dictionary
    for season in observations_by_season:
        season_counts[season] = season_counts[season] + 1

    x_label = ''
    x_label = input('Enter the label for the x-axis (something about seasons): ')
    y_label = ''
    y_label = input('Enter the label for the y-axis (something about number of occurrences): ')
    figtitle = ''
    figtitle = input('Enter the title for your figure: ')
    print("Sit tight, we're making the figure...")

    # plot a histogram of the season_counts dictionary
    plt.bar(season_counts.keys(), season_counts.values())

    # parameters for the figure
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(figtitle)
    plt.tight_layout()

    save_name = ''
    save_name = input('What do you want to call your figure save? ')
    plt.savefig(save_name)
    print("Figure successfully saved!")

    print('Figure can be found at', os.path.abspath(save_name))

visualize_occurrences_by_season()
