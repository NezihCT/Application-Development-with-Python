#  ctrl + k + c => yorum satırına alır
#  ctrl + k + u => yorum satırından alır
#  alt + shift + f => kodları düzenle


# Convert : elinizdeki bir veri tipini fartlı bir veri tipine çevirme işlemi yapar

# int()   : tam sayı veri tipine çevirir
# str()   : string (metinsel) değere çevirme işlemi yapar
# float() : ondalıklı değere çevirme işlemi
# chr()   : verdiğiniz sayısal değerin, karakter karşılığını teslim eder.
# ord()   : verdiğiniz karakterin, ascii (sayısal) karşılığını teslim eder.


# sayi1 = input("Lütfen 1. sayıyı giriniz : ")
# sayi2 = input("Lütfen 2. sayıyı giriniz : ")

# print(sayi1)
# print(type(sayi1))

# print(sayi1 + sayi2)


# toplam = float(sayi1) + float(sayi2)
# print(toplam)

# result = int(sayi1) + int(sayi2)
# print(result)

print(chr(65), ord('A'))
print(chr(90), ord('Z'))
print(chr(97), ord('a'))
print(chr(122), ord('z'))

sayi = 100
print("sayının değeri", sayi)
print("Sayının değeri " + str(sayi))