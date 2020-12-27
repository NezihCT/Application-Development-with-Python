# dışarıdan isim ve soyisim alan bir metot yazınız, metot ilk parametredeki kelimenin ilk 2 farfini büyük, kalanını küçük alsın, 2. parametrenin ise, hepsini küçük alıp a harflerini e ile değiştirip bize @hotmail.com mail adresi olarak teslim etsin


# murat, vuranok
# MUrat.vurenok@hotmail.com


def Mail(firstname, lastname):
    if len(firstname) <= 2:  # girilen isim 2 veya daha az karakter ise. su
        firstname = firstname.upper()
    else:
        firstname = f"{firstname[0:2].upper()}{firstname[2:].lower()}"

    lastname = lastname.lower().replace("a", "e")

    return f"{firstname}.{lastname}@hotmail.com".replace(" ", "")


isim = input("Lütfen adınızı giriniz : ")
soyisim = input("Lütfen soyadınızı giriniz : ")

mail = Mail(isim, soyisim)
print(mail)