from abc import ABCMeta, abstractmethod


class BasePhone(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, marka, model, fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat

    @abstractmethod
    def Sound(self):
        return "telefon sesi"


class Samsung(BasePhone):
    def __init__(self, marka, model, fiyat, tedarikci):
        super().__init__(marka, model, fiyat)
        self.Tedarikci = tedarikci

    def Sound(self):
        return "erik dalı"


class Apple(BasePhone):
    def __init__(self, marka, model, fiyat, garanti):
        super().__init__(marka, model, fiyat)
        self.Garanti = garanti

    def Sound(self):
        return "e 30 a biner"


samsung = Samsung("Note", "Note 20", 15.000, "samsung")
print(f"Samsung telefon sesi {samsung.Sound()}")

apple = Apple("IPhone", "Iphone 12 Pro Max", 30.000, 1)
print(f"Apple telefon sesi {apple.Sound()}")
