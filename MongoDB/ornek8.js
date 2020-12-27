// db oluşturma
use TelefonRehberi


db.Kisiler.insertMany([{
        "firstname": "murat",
        "lastname": "vuranok"
    },
    {
        "firstname": "ahmet",
        "lastname": "şahin"
    }
])

/*
{
    "_id" : ObjectId("5fa693bb6c6d2f0cd313bf8b"),
    "firstname" : "murat",
    "lastname" : "vuranok"
}
{
    "_id" : ObjectId("5fa693bb6c6d2f0cd313bf8c"),
    "firstname" : "ahmet",
    "lastname" : "şahin"
}
*/

db.Telefonlar.drop() // tabloyu siler

db.Telefonlar.insertMany([{
        "name": "work",
        "number": "+901234567890",
        "personId": ObjectId("5fa693bb6c6d2f0cd313bf8b")
    },
    {
        "name": "home",
        "number": "+901234567890",
        "personId": ObjectId("5fa693bb6c6d2f0cd313bf8b")
    },
    {
        "name": "cell",
        "number": "+901234567890",
        "personId": ObjectId("5fa693bb6c6d2f0cd313bf8b")
    }
])

db.Kisiler.aggregate({
    $lookup: {
        from: "Telefonlar",
        localField: "_id",
        foreignField: "personId",
        as: "TelefonNumaralari"
    }
}).pretty()