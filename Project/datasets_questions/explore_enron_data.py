#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data)) # Number of people in the dataset
print(len(enron_data["SKILLING JEFFREY K"]))
count = 0

for j, i in enron_data.items():
	if i["poi"]==True:
		count += 1
print "POI's " + str(count)

poi_people = (open("../final_project/poi_names.txt", "r"))
poi_people.readline()
poi_people.readline()

poi_count = 0
for poi in poi_people:
	poi_count += 1
print(poi_count) # POI's in total

# James Prentice stock value

print enron_data["PRENTICE JAMES"]["total_stock_value"]

# Wesley Colwell e-mail messages to poi's

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Jeffrey K Skilling value of stock options 

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Maximum total payments feature 

print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

# Quantified Salary

print len(dict((key, value) for key, value in enron_data.items() if value["salary"] != 'NaN'))

# Known Email Address

print len(dict((key, value) for key, value in enron_data.items() if value["email_address"] != 'NaN'))