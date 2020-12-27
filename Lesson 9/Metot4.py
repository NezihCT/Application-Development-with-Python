def Metot(**param):
    print(param["Ad"])
    print(param)


Metot(
    Ad="murat",
    Soyad="vuranok",
    Telefon="+901234567890",
    Mail="murat.vuranok@bilgeadam.com"
)


ad = input("lütfen adınızı giriniz : ")
lastname = input("lütfen lastneminizi giriniz : ")
Metot(Ad=ad, Soyad=lastname)