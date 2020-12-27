# __init__ constructor (yapıcı metot) sınıf bir örnek aldığınızda yapılması gereken konfigurasyon vs var ise, __init__ içerisinde tanımlayabilirsiniz.

from datetime import datetime


class Personel:
    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = ""
    CreatedDate = ""
    IkincilAd = ""

    def __str__(self):
        return f"{self.Adi} {self.Soyadi}\nKayıt Eklenme Tarihi : {self.CreatedDate}"

    def __init__(self, isim, soyisim, telefon, mail, ikincilAdi):
        self.CreatedDate = datetime.now()
        self.Adi = isim
        self.Soyadi = soyisim
        self.Telefon = telefon
        self.Mail = mail
        self.IkincilAd = ikincilAdi
        print("__init__ metodu çalıştı")

    def GetInfo(self):
        return f"Adı : {self.Adi}\nSoyadı : {self.Soyadi}"

# init metoduna parametre verdiğinizden dolayı,artık burdaki gibi atama işlemi yapamazsınız.
# personel = Personel()
# personel.Adi = "Murat"
# personel.Soyadi = "Vuranok"
# personel.Mail = f"{personel.Adi}.{personel.Soyadi}@bilgeadam.com"
# personel.Telefon = "2134567"
# print(personel)


personel = Personel("murat", "vuranok", "1234567",
                    "murat.vuranok@bilgeadam.com", "mert")
print(personel)
print(personel.GetInfo())