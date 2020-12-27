import random
import os


class Person():
    FirstName = ""
    LastName = ""
    Phone = ""
    Mail = ""

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    def Find(self, param):
        if param in self.FirstName or \
            param in self.LastName or \
            param in self.Mail or \
            param in self.Phone:

            return True
        else:
            return False


# kişileri tutacağımız  bir dizi (geçici database)

first_names = [
    "Kelly", "Harry", "Lloyd", "Don", "Marilyn", "Henry", "Marcia", "Kim",
    "Lena", "Delores"
]
last_names = [
    "Fleming", "Jimenez", "Pierce", "Howard", "Sanchez", "Sims", "Thomas",
    "Roberts", "Nguyen", "Torres"
]
domain = [
    "hotmail", "bilgeadam", "aof.edu", "sabanci", "gmail", "yahoo", "live",
    "garanti", "teknosa", "nike"
]
people = []
for i in range(10):
    person = Person()
    person.FirstName = first_names[random.randint(0, len(first_names) - 1)]
    person.LastName = last_names[random.randint(0, len(last_names) - 1)]
    person.Mail = f"{person.FirstName}.{person.LastName}@{domain[random.randint(0, len(domain) - 1)]}.com".lower(
    )

    person.Phone = f"+90 (5{random.randint(10,99)}) {random.randint(100,999)} {random.randint(10,99)} {random.randint(10,99)}"

    people.append(person)


def Liste(param):
    os.system("clear")
    index = 0
    if param == "":
        for person in people:
            print("-" * 50)
            print(f"{'Id':<15}: {index}")
            for key, value in person.__dict__.items():
                print(f"{key:<15}: {value}")
            print("-" * 50)
            print()
            index += 1
    else:
        for person in people:
            if (person.Find(param)):
                print("-" * 50)
                print(f"{'Id':<15}: {index}")
                for key, value in person.__dict__.items():
                    print(f"{key:<15}: {value}")
                print("-" * 50)
                print()
            index += 1


go_on = "y"
while go_on == "y":

    key = input("Lütfen arama kelimesi giriniz : ")
    Liste(key)
