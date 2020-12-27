adet = int(input("Kaç adet sayı girmek istiyorsunuz: "))

sayilar_listesi = []
i = 0

if adet > 0 :
    while i < adet :
        sayilar = float(input("Sayıları giriniz: "))
        sayilar_listesi.append(sayilar)
        i += 1
        sayilar_listesi.sort()
else:
    print("Geçersiz.")


büyük_sayi = sayilar_listesi[-1]
büyük_sayi2 = sayilar_listesi[-2]
print("Girilen inputlar arasındaki en büyük sayı: ",büyük_sayi)
print("Girilen inputlar arasındaki en büyük 2. sayı: ",büyük_sayi2)
print("Bu sayıların çarpımı ise ",büyük_sayi * büyük_sayi2)
