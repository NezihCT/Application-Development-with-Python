# Kullanıcın dışarıdan girdiği sayıların toplamını ekrana yazdıran bir uygulama yazınız

# örnek => 123 => 6
import os
os.system("clear")

metin = input("Lütfen sayı giriniz : ")

i = 0
toplam = 0
while i < len(metin):
    toplam += int(metin[i])
    i += 1
print("Girilen sayıların toplamı : {}".format(toplam))