import json
from collections import OrderedDict
import csv

count = 1
a_list = []
a2_list = []
value_list = []
x = 0
file_path_entered = input("Enter the filename to processes   ===>  ")
noc = int(input('Please enter the column numbers  ==>  '))
file_path_csv = file_path_entered + ".csv"
file_path_json = file_path_entered + ".json"
with open(file_path_csv,'w',newline='', encoding='UTF8') as csv_file: ##Open CSV file
    csv_app = csv.writer(csv_file) ##constructor for loading CSV
    with open(file_path_json,'r', encoding='UTF8',buffering=50000000) as f: ##open JSON file, encoded to UTF
        for dict in f:
            f_data = json.loads(dict, object_pairs_hook=OrderedDict) ##Loding Json Data
            for key,value in f_data.items():
                if count <= (noc):
                    a_list.append(key) ##Write header keys to a list
                    count = count + 1
                    if count == (noc +1):
                        csv_app.writerow(a_list) ## Write header to CSV                            
                a2_list.append(value)
                if len(a2_list) == noc:
                    csv_app.writerow(a2_list) ## Write rows to CSV
                    
                    a2_list = [] ## Emptying the list
                    x = x + 1
                    print("Line ", x, " Complete") ## Just to show count
                    
                        


##    with open('review.csv','w') as csv_file:
##        csv_app = csv.writer(csv_file)
##        csv_app.writerow(a_list)
##        print (a_list)
##        for items in value_list:
##            csv_app.writerow(items)
##            print (items)
##    with open('review.csv', 'w') as csv_file:
##        csv_app = csv.writer(csv_file)
##        csv_app.writerow(a_list)
##        print (a_list)

#################################################
   
