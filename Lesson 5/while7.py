sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tek_sayilar = []
cift_sayilar = []

# dizi içerisinde yer alan, tek sayıları bir diziye çift sayıları ayrı bir diziye ekleyiniz. işlem sonunuda toplamda dizi içerisinde kaç eleman var kullanıcıya bildirim veriniz.

# Tek sayıların adedi :

i = 0
while i < len(sayilar):
    if i % 2 == 0:
        cift_sayilar.append(sayilar[i])
    else:
        tek_sayilar.append(sayilar[i])
    i += 1

print(
    f"Tek sayıların toplamı : {len(tek_sayilar)}\nÇift sayıların toplamı : {len(cift_sayilar)}")