# you must run the code in advanced_python_regex.py to get the data  from the faculty.csv file and extract the email list,
# but this is the code that I ran afterward to save the email addresses to a csv file.


# save email addresses to a csv file
with open(savename_path, 'w', newline='') as csvfile:
    writer_obj = csv.writer(csvfile, delimiter=' ')
    [writer_obj.writerow([element]) for element in email_addresses]