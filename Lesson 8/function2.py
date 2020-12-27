# dışarıdan girilen değerin, tek veya çift olma durumunu kontrol ediniz.
# girilen değer, çift ise -1 değerini tek ise, 1 değerini, 0 ise, 0 değerini teslim eden metot yazınız.


def TekCiftKontrolu(sayi):
    result = 0
    if(sayi == 0):
        result = 0
    elif sayi % 2 == 0:
        result = -1
    else:
        result = 1
    return result


def TekCiftKontrolu1(sayi):
    if(sayi == 0):
        return 0
    elif sayi % 2 == 0:
        return -1
    else:
        return 1


result = TekCiftKontrolu(int(input("Lütfen sayı giriniz : ")))

print(result)