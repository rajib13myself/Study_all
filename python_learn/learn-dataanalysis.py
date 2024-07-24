import pandas as pd 
from pymongo import MongoClient

#Read csv file from specific location
rd_file = r"D:\dbt_workspace\python_learn\timetable.csv"
# Define column names (ensure these match your CSV structure)
column_names = ['Week', 'Weekday', 'Begin_date', 'Begin_time', 'End_date', 'End_time', 'Course', 'Programme', 'Group', 'Room', 'Reason', 'Teacher', 'Comment', 'Map', 'Equipment']

df = pd.read_csv(rd_file, names=column_names, skiprows=1)     ## skiprows=1 if the first row is headers

#connect the mongodb
client = MongoClient('mongodb://localhost:27017/')      #Default local db connection


#Create DB and collection
db = client['mytestdb']
collection = db['mytestcollection']

#Insert Data into mongodb
data_dict = df.to_dict(orient='records')        #Convert DataFrame to Dictionary
collection.insert_many(data_dict)

print("Data load successfully in MongoDB")