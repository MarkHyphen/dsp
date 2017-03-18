# again, you must run the code in advanced_python_regex.py to get the data from the faculty.csv file which is then reformated into the asked
# for dictionaries.  Essentially you should append together advanced_python_regex.py then advanced_python_dict.py into a single file for 
# this to run properly



for i in range(len(imported_data)):
    temp = imported_data[i]['name'].split()
    imported_data[i]['first_name'] = temp[0]
    imported_data[i]['last_name'] = temp[-1]
    if len(temp)>2:
        imported_data[i]['middle_initial'] = temp[1]
    else:
        imported_data[i]['middle_initial'] = ''
    temp_insert = 0
faculty_dict = {element['last_name']: [element['degree'], element['title'], element['email']] for element in imported_data}

#I feel like this is a total hack.  There must be a better way to sort by individual components of the key tuple.  Could not find anything
# even remotely helpful on the internet.  Unless you start using alternative methods such as creating an ordered dictionary.  I fugured
# these is probably a very simple way of doing this that is evading me using nothing but what is available within the python core
# rather than importing some special module.
professor_dict = {(element['first_name'], element['last_name']): [element['degree'], element['title'], element['email']] for element in imported_data}
prof_names = [k for k in professor_dict1.keys()]
prof_names.sort(key=lambda x: x[1])
for i in range(len(prof_names)):
    print(str(prof_names[i]) + '\t:\t' + str(professor_dict1[prof_names[i]]))