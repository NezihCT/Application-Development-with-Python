# kullanıcı input aracılığıyla uygulamaya sayı girecek, veee kullanıcı dilediği kadar sayı girebilir şokkkkk :)

# her sayı girildiğinde kullanıcıya yeni bir sayı girecekmisin? diye sorulacak, kullanıcı y tuşuna basarsa lütfen sayı giriniz diyip içeriye sayı alınacak

# kullanıcı harici bbir tuşa basarsa, içeride yer alan tek sayıların en küçük ve en büyük sayısının birbirine olan farkını geriye dönsün :

import os


def FarkHesapla():
    go_on = "y"
    tek_sayilar = []
    while go_on == "y" or go_on == "Y":
        number = float(input("Lütfen sadece sayısal değer giriniz : "))
        os.system('clear')
        if number % 2 != 0:
            tek_sayilar.append(number)
        go_on = input("yeni bir sayı eklemek istiyormusunuz (Y\\N) : ")
        os.system('clear')
    return max(tek_sayilar) - min(tek_sayilar)


sonuc = FarkHesapla()
print("İşlem sonucu :", sonuc)
