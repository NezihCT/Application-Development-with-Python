# birden fazla elemanla çalışacak ise, tek tek değişken tanımlamak yerine, dizi kullanıyoruz.
# Tanımlama şekli
sehirler = ["istanbul", "edirne", "konya", "rize",
            "ankara", "eskişehir", "adana", "kayseri", "Bursa"]


# Not : bir dizinin maximum index değeri, o dizinin elaman sayısı(uzunluğu) 1- değeridir

# 1 2 3 4 5 6 7 8  => eleman sayısı
# 0 1 2 3 4 5 6 7  => o elemanın dizi içerisindeki index değeridir.

# eleman sayı  => dizi içerisindeki toplam adet
# index değeri => dizi içerisinde yer alan, herhagi bir elemana ulaşma şekli

print(sehirler[0])  # dizinin ilk elemanını ekrana yazdırdık.

# dizinin son elemanını ekrana yazdırınız
index = len(sehirler)  # toplam eleman sayısını teslim eder

index = len(sehirler) - 1  # o dizinin maximun index değerini teslim eder.
print(sehirler[index])

print(sehirler[2:7])
# 1. parametrede verilen index değeri(dahil) nerden başlayacağım
# 2. parametrede verilen index değerinin bir alt değerine kadar olan elemanları listeler


# dizinin tüm elemanlarını ekrana yazdırmak istersek?
print(sehirler[:])

# adana parametresi, dizi içerisinde geçmektemidir, geçmemektemidir.
print('adana' in sehirler)

# kullanıcı dışarıdan şehir adı girecek, var ise bu şehir dizi içerisinde yer almaktadır, yok ise, bu dizi şehir içerisinde yer almamaktadır. mesajını veriniz :)


sehir = input("Lütfen şehir adı giriniz : ")
mesaj = ""
# if sehir in sehirler:
#     mesaj = f"parametrede gönderdiğiniz {sehir} sehri, dizi içerisinde yer almaktadır"
# else:
#     mesaj = f"parametrede gönderdiğiniz {sehir} sehri, dizi içerisinde yer almamaktadır"

# print(mesaj)

result = f"parametrede gönderdiğiniz {sehir} sehri, dizi içerisinde yer almaktadır" if sehir in sehirler else f"parametrede gönderdiğiniz {sehir} sehri, dizi içerisinde yer almamaktadır"

# ternary opt.
# koşul içerisinde true dönerse, soldaki alan, false dönerse sağdaki alan çalışır.

# print(result)

print(
    f"parametrede gönderdiğiniz {sehir} sehri, dizi içerisinde yer alma{ '' if sehir in sehirler else 'ma' }ktadır")


print("parametrede gönderdiğiniz {} sehri, dizi içerisinde yer alma{}ktadır".format(
    sehir, ("" if sehir in sehirler else "ma")))


myList1 = ["sehirler dizisi"]
print(myList1)

myList2 = ["arabalar dizisi"]
print(myList2)

myList3 = ["renkler dizisi"]
print(myList3)

result = list(zip(myList1, myList2, myList3))
print(result)