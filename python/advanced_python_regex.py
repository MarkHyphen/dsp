import os
import csv
import re
from collections import namedtuple

# this function extracts the data, corrects any extra spaces found in the keynames, and returns the data as a list of
# dictionaries
def get_data(path_to_data):
    list_of_dicts=[]
    with open(path_to_data, 'r', newline='\n') as fname:
        data = csv.DictReader(fname, delimiter=',')
        for i in range(len(data.fieldnames)):
            data.fieldnames[i] = re.sub(r'^ ', '', data.fieldnames[i])
        return [row_data for row_data in data]



# this function takes in the data and finds the counts of the various degree types
def find_count(data, regex_list, data_key):
    passed_data = ''
    passed_data = passed_data + str([row_data[data_key] for row_data in data])
    passed_data = re.sub(r'\'(?P<tag>[ \w\d.]*)\'', '\g<tag>', passed_data)
    passed_data = re.sub(r'([\[\],])', '', passed_data)
    passed_data = re.sub(r' (of|Biostatistics|is)', '', passed_data)
    passed_data = re.sub(r'Associate Professor', 'Associate_Professor', passed_data)
    passed_data = re.sub(r'Assistant Professor', 'Assistant_Professor', passed_data)
    passed_data = passed_data.split()
    data_counts = [0] * (len(regex_list))
    for i in range(len(regex_list)):
        data_counts[i] = [data_counts[i] + 1 for element in passed_data if re.match(regex_list[i], element)]
        data_counts[i] = sum(data_counts[i])
    return data_counts

# this function extracts all the various degrees and their variations in abbreviations as well as titles, then creates and returns a list of regex
# expressions that will capture these data.
def find_types(data, data_key):
    degrees_had = []
    passed_data = ''
    passed_data = passed_data + str([row_data[data_key] for row_data in data])
    passed_data = re.sub(r'\'(?P<tag>[ \w\d.]*)\'', '\g<tag>', passed_data)
    passed_data = re.sub(r'([\[\],])', '', passed_data)
    passed_data = re.sub(r' (of|Biostatistics|is)', '', passed_data)
    passed_data = re.sub(r'Associate Professor', 'Associate_Professor', passed_data)
    passed_data = re.sub(r'Assistant Professor', 'Assistant_Professor', passed_data)
    passed_data = passed_data.split()
    passed_data = list(set(passed_data))
    passed_data.sort(key = len)
    while len(passed_data) != 0:
        element_of_interest = passed_data.pop()
        ind_flag = 0
        ind_periods = []
        while ind_flag >= 0:
            ind_flag = element_of_interest.find('.', ind_flag+1)
            ind_periods.append(ind_flag)
        RE_search_str = ''
        start_ind = 0
        if (len(ind_periods) == 1):
            RE_search_str = element_of_interest
            degrees_had.append(RE_search_str)
        else:
            for i in range(len(ind_periods)-1):
                RE_search_str = RE_search_str + element_of_interest[start_ind:ind_periods[i]+1] + '?'
                start_ind = ind_periods[i]+1
            current_temp_len = len(passed_data)
            RE_obj = re.compile(RE_search_str)
            matched = [RE_obj.match(element) for element in passed_data]
            to_remove = []
            [to_remove.append(i) for i, element in enumerate(matched) if element]
            [passed_data.pop(element) for element in to_remove[::-1]]
            degrees_had.append(RE_search_str)
    return degrees_had


def make_email_list(data):
    email_list = [element['email'] for element in data]
    return email_list


filepath = '/home/nazgul/Dropbox/MP_Documents/Courses/Metis/metisgh/prework/dsp/python/'
filename = 'faculty.csv'
filename_path = os.path.abspath(os.path.join(filepath, filename))

savepath = '/home/nazgul/Dropbox/MP_Documents/Courses/Metis/metisgh/prework/dsp/python/'
savename = 'emails.csv'
savename_path = os.path.abspath(os.path.join(savepath, savename))

imported_data = get_data(filename_path)

# script to find degrees and compute their counts within the faculty
found_degree_types = find_types(imported_data, 'degree')
counts_degree = find_count(imported_data, found_degree_types, 'degree')
[print(str(found_degree_types[i]) + '\t:\t' + str(counts_degree[i])) for i in range(len(found_degree_types))]

# script to find titles and compute their counts within the faculty
found_title_types = find_types(imported_data, 'title')
counts_titles = find_count(imported_data, found_title_types, 'title')
print('')
[print(str(found_title_types[i]) + '\t:\t' + str(counts_titles[i])) for i in range(len(found_title_types))]

#get email address, make a list, and print list
email_addresses = make_email_list(imported_data)
print('')
[print(element) for element in email_addresses]

# extract the various domains within faculty emails
unique_domains_data = [re.match(r'[\w\d.]*@([\w\d.]*)$', element) for element in email_addresses]
unique_domains = [element.group(1) for element in unique_domains_data]
unique_domains = set(unique_domains)
print('')
[print(element) for element in unique_domains]