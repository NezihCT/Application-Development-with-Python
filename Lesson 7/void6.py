# dışarıdan kullanıcının adını ve soyadını alan bir metot yazınız. metot aldığı bu değerleri kullanarak bize mail adresi oluştursun

# isim.soyisim@hotmail.com

def CreateMail(isim, soyisim):
    mail = f"{isim}.{soyisim}@hotmail.com".lower()
    print(mail)


def MailAdres(isim, soyisim=None):
    if soyisim is None:
        mail = f"{isim}@hotmail.com"
    else:
        mail = f"{isim}.{soyisim}@hotmail.com".lower()
    print(mail)
# adi = input("Lütfen adınızı giriniz : ")
# soyadi = input("Lütfen soyadınızı giriniz : ")
# CreateMail(adi, soyadi)


MailAdres("murat", "vuranok")
MailAdres("murat")