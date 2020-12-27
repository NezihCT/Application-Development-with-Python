  
import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')
myDb = myClient["PhoneBook"]
myCollection = myDb["People"]

person = {
    "firstname": "murat",
    "lastname": "vuranok",
    "phone": "+901234567890",
    "mail": "murat.vuranok@bilgeadam.com"
}

# myCollection.insert_one(person)
# print(myClient.list_database_names())  => server içerisinde yer alan db'lerin isimlerini teslim eder

kisi_id = myCollection.insert_one(person).inserted_id
print(kisi_id)  # 5fa6aa814b5b67395ad22a4f
people = myCollection.find({}, {"firstname": 1, "lastname": 1, "_id": 0})
for i in people:
    print("_" * 40)
    for x, y in i.items():
        print(f"{x} : {y}")
