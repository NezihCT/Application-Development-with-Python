# soyut sınıf
from abc import ABCMeta, abstractmethod


class CoreEntity(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Insert(self):
        print("personelin kaydı eklendi")


class Personel(CoreEntity):
    def Insert(
        self
    ):  # çıktı => Personel Insert Metodu override etmek, üst sınıftan gelen değeri ezerek bizim ihtiyacımız olan şekliyle değiştiriyoruz.
        print("Personel ekleme metodu")


class Kategori(CoreEntity):
    def Insert(self):
        print("Kategori ekleme metodu")


personel = Personel()
personel.Insert()  # CoreEntity sınıfı içerisinde yer alan metot

kategori = Kategori()
kategori.Insert()  # CoreEntity sınıfı içerisinde yer alan metot