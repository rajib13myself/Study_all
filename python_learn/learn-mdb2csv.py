from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mytestdb']
collection = db['mytestcollection']

# Fetch data
data = collection.find()
df = pd.DataFrame(list(data))

# Save to CSV
df.to_csv('data.csv', index=False)
