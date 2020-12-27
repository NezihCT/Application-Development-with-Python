from Person import Person
from PersonService import *
import os


def Create():
    per = Person()
    per.FirstName = input("Lütfen Kişinin Adını Giriniz : ")
    per.LastName = input("Lütfen Kişinin Soyadını Giriniz : ")
    per.Phone = input("Lütfen Kişinin Telefon Numarasını Giriniz : ")
    per.Mail = input("Lütfen Kişinin Mail Adresini Giriniz : ")
    return per


def Start():
    key = "y"
    while key != "e":
        print("Lütfen işlem seçiniz!\nKayıt Ekleme : a\nKayıt Silme : d\nKayıt Listesi : l\nKayıt Güncelle : u")
        key = input("İşlem : ").lower()

        if key == "a":
            person = Create()
            Add(person)
            os.system("clear")
            print("Kayıt başarıyla eklendi!")

        elif key == "d":
            print("Lütfen _id değerini giriniz : ")
            id = input("_id : ")
            Delete(id)
            print("Kayıt başarıyla silindi!")

        elif key == "l":
            List()
        elif key == "u":
            print("Lütfen _id değerini giriniz : ")
            id = input("_id : ")
            Update("")
            print("Kayıt başarıyla silindi!")

Start()