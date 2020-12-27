  
# Aritmetik operatorler

# +, -, /, *, %

# sayi1 = 120
# sayi2 = 50

# toplam = sayi1 + sayi2
# print("İşlem Sonucu" + " "*50 + str(toplam))
# print(("İşlem Sonucu" + " "*50), toplam)


sayi1 = float(input("Lütfen 1. sayıyı giriniz : "))
sayi2 = float(input("Lütfen 2. sayıyı giriniz : "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
bolum = sayi1 / sayi2
mod = sayi1 % sayi2
carpim = sayi1 * sayi2
kuvvet = sayi1 ** sayi2

result = "Toplama İşlemi Sonucu : " + \
    str(toplam) + "\nÇıkartma İşlemi Sonucu : " + \
    str(fark) + "\nBölme İşlemi Sonucu : " + str(bolum) + \
    "\nMod İşlemi Sonucu : " + \
    str(mod)+"\nKuvvet Alma İşlemi Sonucu : " + \
    str(kuvvet)+"\nÇarpma İşlemi Sonucu : " + str(carpim)

res = "Toplama İşlemi :", toplam, "\nÇıkartma İşlemi :", fark

print(result)


# git add *
# git commit -m "açıklama alanı ekleyin"
# git push -u origin master