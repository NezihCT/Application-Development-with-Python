# dictionary()  key value formatında dataları listelemek için kullanılır. Json formatında data tutar, WebApi (servisler), JavaScript, Angular,React(js-native), mongodb gibi birçok platform desteklemektedir.

personeller = [
    {
        "id": 1,
        "indexNo": 0,
        "firstname": "murat",
        "lastname": "vuranok",
        "mail": "murat.vuranok@bilgeadam.com",
        "phone": "+905554443322",
        "phones": [
            {
                "no": "12312321",
                "title": "work",
                "description": ""
            },
            {
                "no": "12312321",
                "title": "school",
                "description": ""
            },
            {
                "no": "12312321",
                "title": "home",
                "description": ""
            }
        ]
    },
    {
        "id": 2,
        "indexNo": 1,
        "firstname": "mehmet",
        "lastname": "civelek",
        "mail": "mehmet.civelek@bilgeadam.com",
        "phone": "+905554443322"
    }
]


print(personeller[0])

# {'id': 1, 'firstname': 'murat', 'lastname': 'vuranok', 'mail': 'murat.vuranok@bilgeadam.com', 'phone': '+905554443322', 'phones': [{'no': '12312321', 'title': 'work', 'description': ''}]}


print(personeller[0]["phones"])
# [{'no': '12312321', 'title': 'work', 'description': ''}]
# [{'no': '12312321', 'title': 'work', 'description': ''}, {'no': '12312321', 'title': 'school', 'description': ''}, {'no': '12312321', 'title': 'home', 'description': ''}]

print(personeller[0]["phones"][0]["no"])
# {'no': '12312321', 'title': 'work', 'description': ''},


# print(personeller[0]["firstname"])


users = [["ceo", "123"], ["admin", "123"], ["user", "123"]]  # => list

kullanicilarin = [
    {"username": "admin", "password": "123"},
    {"username": "ceo", "password": "123"},
    {"username": "moderator", "password": "123"}
]

print(users[0])  # ceo
print(users[0][0])  # ceo
print(users[0][1])  # ceo

print(kullanicilarin[0])  # {'username': 'admin'}
print(kullanicilarin[0]["username"])  # admin
print(kullanicilarin[0]["password"])  # admin


# dictionary içerisinde yer alan bir kaydı güncellemek isterseniz

i = 0  # hangi eleman güncellenecek
key = "firstname"
value = "şahin"

oldRecord = personeller[i][key]

personeller[i][key] = value

newRecord = personeller[i][key]
print(oldRecord)
print(newRecord)


firstname = input("Lütfen adınızı giriniz : ")
lastname = input("Lütfen soyadınızı giriniz : ")
# mail = input("Lütfen mail giriniz : ")
phone = input("Lütfen telefon giriniz : ")

id = len(personeller)
indexNo = len(personeller) - 1

personeller.append({
    "id": id,
    "indexNo": indexNo,
    "firstname": firstname,
    "lastname": lastname,
    "mail": f"{firstname}.{lastname}@bilgeadam.com",
    "phone": phone
})

print(personeller[len(personeller) - 1])

# {'id': 2, 'indexNo': 1, 'firstname': 'mustafa', 'lastname': 'sahin', 'mail': 'mustafa.sahin@bilgeadam.com', 'phone': '123123123'}
