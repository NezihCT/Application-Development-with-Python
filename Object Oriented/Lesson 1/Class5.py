import os
from datetime import datetime
from datetime import timedelta


class Employee:
    FirstName = ""
    LastName = ""
    Mail = ""
    Phone = ""
    # işe giriş tarihi sistem tarafından otomatik eklenecek
    HireDate = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year} {datetime.now().hour}:{datetime.now().minute}"
    FireDays = 0
    Address = ""

    def IseAl(self):

        fireDate = 0
        if(self.FireDays > 0):
            time = (datetime.now() + timedelta(days=self.FireDays))
            fireDate = f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute}"
        else:
            fireDate = "Gün sayısı belirtirlemediğinden, çıkış tarihi hesaplanamadı"

        os.system("clear")
        # os.system("cls") => windows

        print("-"*50, "\n")
        print(
            f"Personelin Adı : {self.FirstName}\nPersonelin Soyadı : {self.LastName}\nPersonelin Mail : {self.Mail}\nPersonelin Telefon : {self.Phone}\nPersonelin Adresi : {self.Address}\nPersonelin İşe Giriş Tarihi : {self.HireDate}\nPersonelin Sözleşme Bitiş Tarihi : {fireDate}\nPersonelin işe girişi yapıldı")
        print("\n", "-"*50)

    def Update(self):
        #db içerisinden personeli güncelle
        pass

    def Fire(self):
        # Personelin db içerisindeki durumun değiştirilmesi
        # 1 = Aktif, 2 = Pasif, 3 = Delete, 4 = Kovuldu, 5 = İşten Çıkarıldı
        pass


personel = Employee()
personel.FirstName = "Murat"
personel.LastName = "VURANOK"
personel.Mail = "murat.vuranok@bilgeadam.com"
personel.Phone = "+901234567890"
personel.Address = "İstanbul / Beşiktaş"
personel.FireDays = 120
personel.IseAl()
