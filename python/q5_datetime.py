# Hint:  use Google to find python function

from datetime import datetime
####a) 
date_start = '01-02-2013'    
date_stop = '07-28-2015'
date_start_obj = datetime.strptime(date_start, '%m-%d-%Y')
date_stop_obj = datetime.strptime(date_stop, '%m-%d-%Y')
time_diff = date_stop_obj-date_start_obj
print(time_diff)

####b)  
from datetime import datetime
date_start = '12312013'    
date_stop = '05282015'
date_start_obj = datetime.strptime(date_start, '%m%d%Y')
date_stop_obj = datetime.strptime(date_stop, '%m%d%Y')
time_diff = date_stop_obj-date_start_obj
print(time_diff)

####c)  
from datetime import datetime
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'
date_start_obj = datetime.strptime(date_start, '%d-%b-%Y')
date_stop_obj = datetime.strptime(date_stop, '%d-%b-%Y')
time_diff = date_stop_obj-date_start_obj
print(time_diff)