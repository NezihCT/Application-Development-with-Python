from random import randint
import os
os.system("clear")

# sayısal loto, benzersiz, 6 adet sayı 8 kolon :)

counter = int(input("Lütfen kolon adedi giriniz : "))
index = 0

while index < counter:
    sayilar = []
    i = 0
    while i < 6:
        sayi = str(randint(1, 49))
        if sayi in sayilar:
            # i -= 1
            continue
        else:
            if(len(sayi) == 1):
                sayilar.append("0" + sayi)
            else:
                sayilar.append(sayi)
        i += 1

    sayilar.sort()
    print(f"{index + 1}. kolon = ", " - ".join(sayilar))
    index += 1
    
# 1. kolon =  17 19 24 26 34 44
# 1. kolon =  13-21-26-29-31-46
# 1. kolon =  11 - 17 - 26 - 45 - 46 - 49
