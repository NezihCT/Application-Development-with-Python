# Parametre alan metotlar
# aldığı parametreye göre, işlem seyrini değiştiren yapılardır.
# Kural 1) Kesinlikle metot içerisinde parametrenin nerden geleceği tanımlanmaz
# Kural 2) Kesinlikle metot içerisinde parametreye değer atanmaz

# Dışarıdan alınan 2 sayıyı ekrana yazdıran metot

def Hesapla(sayi1, sayi2):
    toplam = sayi1 + sayi2
    print(toplam)


Hesapla(10, 10)

s1 = int(input("Lütfen 1. sayıyı giriniz : "))
s2 = int(input("Lütfen 2. sayıyı giriniz : "))

Hesapla(s1, s2)