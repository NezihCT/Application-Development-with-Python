from enum import Enum, auto, Flag


# flag olarak işaretlediğinizde yine enum'dır fakat index numaralı benzersiz ve birden fazla enum değerinin toplamı içerdeki bir enum değerine karşılık gelmemelidir. + bir enum değerine birden fazla enum değeri yükleyebilirsiniz.
class Renkler(Flag):  # enum       flag
    Kirmizi = auto()  # 1           1
    Sari = auto()  # 2              2
    Mavi = auto()  # 3              4
    Pembe = auto()  # 4             8
    Yesil = auto()  # 5             16
    Beyaz = auto()  # 6             32
    Turuncu = auto()  #7            64
    GokKusagi = Kirmizi | Mavi | Turuncu | Pembe  # index değeri 77'dir içerisinde aldığı enum değerlerinin index değerlerinin toplamını kendine index numarası olarak atar,


# [<Renkler.Kirmizi: 1>, <Renkler.Sari: 2>, <Renkler.Mavi: 3>, <Renkler.Pembe: 4>, <Renkler.Yesil: 5>, <Renkler.Beyaz: 6>, <Renkler.Turuncu: 7>]

# [<Renkler.Kirmizi: 1>, <Renkler.Sari: 2>, <Renkler.Mavi: 4>, <Renkler.Pembe: 8>, <Renkler.Yesil: 16>, <Renkler.Beyaz: 32>, <Renkler.Turuncu: 64>]

# [<Renkler.Kirmizi: 1>, <Renkler.Sari: 2>, <Renkler.Mavi: 4>, <Renkler.Pembe: 8>, <Renkler.Yesil: 16>, <Renkler.Beyaz: 32>, <Renkler.Turuncu: 64>, <Renkler.GokKusagi: 77>]

liste = list(Renkler)

print(liste)