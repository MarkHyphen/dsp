# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


# I am assuming that since this is kind of "python intro" stuff that we shouldn't be using numpy or pandas
# so I am purposely not doing so for this code and trying to not used more advanced packages to manipulate
# the data.

import os
import csv
import operator

def get_data(path_to_data):
    list_of_dicts=[]
    with open(path_to_data, 'r', newline='\n') as fname:
        data = csv.DictReader(fname, delimiter=',')
        return [row_data for row_data in data]

def get_team_with_smallest_diff(list_of_dicts):
    diff_for_v_agains = []
    team_name = []
    for row_data in list_of_dicts:
        diff_for_v_agains.append(abs(int(row_data['Goals'])-int(row_data['Goals Allowed'])))
        team_name.append(row_data['Team'])
    min_index, min_value = min(enumerate(diff_for_v_agains), key=operator.itemgetter(1))
    return team_name[min_index]




filepath = '/home/nazgul/Dropbox/MP_Documents/Courses/Metis/metisgh/prework/dsp/python/'
filename = 'football.csv'
filename_path = os.path.abspath(os.path.join(filepath, filename))

all_data = get_data(filename_path)
min_team = get_team_with_smallest_diff(all_data)
print(min_team)
