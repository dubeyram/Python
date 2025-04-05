# pymongo==4.11.3
from pymongo import MongoClient

# Connect to local MongoDB (default port 27017)
client = MongoClient("mongodb://localhost:27017/")

# Select database and collection
db = client["MongoLearning"]
collection = db["teachers"]


#-------------------------------------------------------------------------------
# Inserting Documents
#-------------------------------------------------------------------------------

teacher = {
    "name": "John Doe",
    "age": 40,
    "gender": "Male",
    "subjects": ["Math", "Science"],
}

result = collection.insert_one(teacher)
print(result)

#-------------------------------------------------------------------------------
# Updating Documents
#-------------------------------------------------------------------------------

update = {"$set": {"age": 41}}
result = collection.update_one({"name": "John Doe"}, update)
print(result)

#-------------------------------------------------------------------------------
# Deleting Documents
#-------------------------------------------------------------------------------

result = collection.delete_one({"name": "John Doe"})
print(result)

#-------------------------------------------------------------------------------
# Querying Documents
#-------------------------------------------------------------------------------

# Find all documents
cursor = collection.find()
for document in cursor:
    print(document)
    break

# Find documents with specific field
cursor = collection.find({"age": {"$gt": 40}})
for document in cursor:
    print(document)
    break

# Find documents with specific field range
cursor = collection.find({"age": {"$gt": 40, "$lt": 50}})
for document in cursor:
    print(document)
    break

# Find documents with specific field value
cursor = collection.find({"age": 41})
for document in cursor:
    print(document)
    break

# Find documents with specific field value and return only the "_id" field
cursor = collection.find({"age": 41}, {"_id": 1})
for document in cursor:
    print(document)
    break


#Find documents with specific field value and return only the "_id" and "name" fields
cursor = collection.find({"age": 41}, {"_id": 0})
for document in cursor:
    print(document)
    break

# Limit and skip documents
cursor = collection.find({"age": 41}, {"_id": 0}).limit(2).skip(1)
for document in cursor:
    print(document)
    

#-------------------------------------------------------------------------------
# Aggregation
#-------------------------------------------------------------------------------

pipeline = [
    {"$match": {"age": {"$ne": 40}}},
    {"$group": {"_id": "$name" ,"count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
]

# Find all documents based on the pipeline
cursor = collection.aggregate(pipeline)
for document in cursor:
    print(document)
    break

# Limit the number of documents
pipeline.append({"$limit": 2})
cursor = collection.aggregate(pipeline)
for document in cursor:
    print(document)
    break

# Skip the first document
pipeline.append({"$skip": 1})
cursor = collection.aggregate(pipeline)
for document in cursor: 
    print(document)
    break