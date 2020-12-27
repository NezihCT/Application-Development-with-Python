import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')
myDb = myClient["PhoneBook"]
people = myDb["People"]
phones = myDb["Phones"]

person = {
    "firstname": "murat",
    "lastname": "vuranok",
    "phone": "+901234567890",
    "mail": "murat.vuranok@bilgeadam.com"
}

# people.insert_one(person)

# kisi_id = people.insert_one(
#     person).inserted_id  # kaydı ekledikten sonra objectID değerini teslim eder

# phones_numbers = [{
#     "name": "work",
#     "phone": "+901234567890",
#     "personId": kisi_id
# }, {
#     "name": "home",
#     "phone": "+901234567890",
#     "personId": kisi_id
# }, {
#     "name": "cell",
#     "phone": "+901234567890",
#     "personId": kisi_id
# }]

# phones.insert_many(phones_numbers)

# for p in people.find({}, {"_id": 0}):
for p in people.find():
    print("-" * 40)
    print()
    for x, y in p.items():
        print(f"{x:10} : {y}")

    telefon_numaralari = phones.find({"personId": p["_id"]}, {
        "_id": 0,
        "personId": 0
    })
    for t in telefon_numaralari:
        for c, d in t.items():
            print(f"            {c:10} : {d}")
    print("_" * 40)