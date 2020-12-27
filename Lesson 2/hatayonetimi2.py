try:
    sayi_bir = int(input("Lütfen 1. sayıyı giriniz : "))
    sayi_iki = int(input("Lütfen 2. sayıyı giriniz : "))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    carpim = sayi_bir * sayi_iki
    bolum = sayi_bir / sayi_iki
    mod = sayi_bir % sayi_iki

    print(
        f"Sayıların Toplamı : {toplam}\nSayıların Farkı : {fark}\nSayıların Bölümü : {bolum}\nSayıların Bölüm Farkı : {mod}\nSayıların Çarpımı : {carpim}")

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except FileExistsError:
    print("FileExistsError")
except:
    print("Tüm hataları kabul ediyorum, özür dilerim")