def Metot(**param):
    print("-"*45)
    for key, value in param.items():
        print("{:8} : {}".format(key, value))
    print("-"*45)


Metot(
    Ad="murat",
    Soyad="vuranok",
    Telefon="+901234567890",
    Mail="murat.vuranok@bilgeadam.com"
)