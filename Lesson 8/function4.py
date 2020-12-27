# dışarıdan bir sayısal dizi alacak, metot parametredeki yer alan elemanların toplamının karekökünü geriye teslim etsin

import math


def Hesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return math.sqrt(toplam)


dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = Hesapla(dizi)
print(result)
