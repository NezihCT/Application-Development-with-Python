# örnek 1) dışarıdan alınan 2 sayının toplamıyla farkının bölümünden kalanı kaçtır

# sayi1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
# sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))

# toplam = sayi1 + sayi2
# fark = sayi1 - sayi2
# mod = toplam % fark

# result = (sayi1 + sayi2) % (sayi1 - sayi2)
# print("işlem sonucu :", result)
# print("İşlem sonucu :", mod)

# ---------------------------------------------------

# örnek 2) dışarıdan girilen bir sayının 10 eksiğinin 20 fazlasının ikiye bölümünden kalan kaçtır


# sayi = int(input("Lütfen sayı giriniz : "))
# 1)
# sayi = sayi - 10
# sayi = sayi + 20
# sayi = sayi % 2
# print("İşlem sonucu :", sayi)

# 2)
# sayi = ((sayi - 10) + 20) % 2
# print("işlem sonucu :", sayi)
# ---------------------------------------------------

# örnek 3) dışarıdan girilen iki sayının karelerinin toplamı ile karelerinin farkı toplamı kaçtır.

# sayi1 = int(input("Lütfen 1. sayıyı giriniz : "))
# sayi2 = int(input("Lütfen 2. sayıyı giriniz : "))

# kare1 = sayi1**2
# kare2 = sayi2**2

# toplam = kare1 + kare2
# fark = kare1 - kare2
# print("İşlem sonucu :", (toplam + fark))

# örnek 4) Vize notu %30, final notu %70'ini alıp not ortalamasını hesaplayıp kullanıcıya aldığı not'u gösteriniz

# not_vize = float(input("Lütfen vize notunuzu giriniz : "))
# not_final = float(input("Lütfen final notunuzu giriniz : "))

# _not = (not_vize * 0.30) + (not_final * 0.70)
# print("Not ortalamanız :", _not)

# örnek 5) Kullanıcı ilk olarak adını, 2 olarak ise soyismini girsin, işlem sonunda kullanıcıya   isim.soyisim@hotmail.com şeklimnde mail adersini teslim ediniz.

isim = input("Lütfen adınızı giriniz : ")
soyisim = input("lütfen soyadınızı giriniz : ")

mail = "{}.{}@hotmail.com".format(isim, soyisim)
mail1 = f"{isim}.{soyisim}@hotmail.com"
test = isim + "." + soyisim + "@hotmail.com"
print(mail1)

# string.format("{1}.{0}@hotmail.com",isim,soyisim)
# $"{isim}.{soyisim}@hotmail.com"
# `${isim}.${soyisim}@hotmail.com`

print(mail)