class Personel:
    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = ""
    Yas = 0

    # __str__ metodu default olarak sınıfın adını ve ram üzerindeki adresini teslim eder. siz __str__ medodunu override (yeniden yazma) işlemi yaparsanız, sizin geriye döndüğünüz değer ekranda görünüyor olacak

    def __str__(self):
        return f"{self.Adi} {self.Soyadi}"


personel = Personel()
personel.Adi = "Murat"
personel.Soyadi = "Vuranok"
personel.Telefon = "12345678"
personel.Yas = 100
personel.Mail = "murat.vuranok@bilgeadam.com"

# sınıftan aldığınız örneği direkt olarak print ederseniz size ram üzerinde tuttuğu adresi teslim eder. <__main__.Personel object at 0x105978a50>
print(personel)
