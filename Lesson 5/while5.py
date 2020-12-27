# Kullanıcının panel üzerinden girdiği metni alt alta yazdırınız.
import os
os.system('clear')


metin = input("lütfen bir metin giriniz : ")
index = 0
while index < len(metin):
    print(metin[index])
    index += 1