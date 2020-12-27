# 1 ile 1000 arasındaki sayıların toplamını ekrana yazdıran metot yazınız

def Hesapla():
    toplam = 0
    for sayi in range(1, 1001):
        toplam += sayi
    print(toplam)


Hesapla()