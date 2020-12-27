# dışarıdan girilen metin içerisinde yer alan sesli ve sessiz harfleri ayrıştırınız ve kullanıcıya toplam adetlerini gösteriniz

sesli_harfler = ["a", "i", "ı", "e", "o", "ö", "u", "ü"]
sesli = []
sessiz = []

metin = input("Lütfen metin giriniz : ")

i = 0
while i < len(metin):
    karakter = metin[i]
    # if karakter in sesli_harfler:
    if sesli_harfler.count(karakter):
        sesli.append(karakter)
    else:
        sessiz.append(karakter)
    i += 1

print(
    f"Metin içerisinde toplam sesli harf sayısı : {len(sesli)}\nMetin içerisinde toplam sessiz harf sayısı : {len(sessiz)}")
