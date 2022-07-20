import pymongo
client = pymongo.MongoClient("mongodb+srv://maityanubhab:Anubhab9564@cluster0.mlojg5z.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhangsu",
    "email":"sudhangsu@ineuron.ai",
    "surname":"kumar"
}

db1 = client['mongotest']
coll = db1["test"]
coll.insert_one(d)

vgg
ghvgvgv

gvgvgv