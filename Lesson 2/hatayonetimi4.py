try:
    sayi1 = int(input("Lütfen sayı giriniz : "))
    sayi2 = int(input("Lütfen sayı giriniz : "))
    sonuc = sayi1 / sayi2

except ValueError as mahmud:
    print("İşlem hatası")
else:
    try:
        print(sayi1 / sayi2)
        print("İşlem sonucu")
    except ZeroDivisionError as mahmud:
        print(mahmud)