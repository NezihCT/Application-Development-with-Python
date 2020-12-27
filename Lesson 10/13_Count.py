# .count() => parametrede verdiğiniz değerin, metin içerisinde kaç adet olduğunu teslim eder.

metin = "bilge adam beşiktaş"

sonuc = metin.count('b')
print(
    f"parametrede gönderdiğiniz değer, metin içerisinde {sonuc} kadar geçmektedir")  # sonuc = 2

sehirler = ["ankara", "edirne", "eskişehir",
            "urfa", "adana", "bursa", "eskişehir"]
param = "eskişehir"
result = sehirler.count(param)

print(f"{param} anahtar kelimesi dizi içerisinde toplamda {result} defa içermektedir.")
# eskişehir anahtar kelimesi dizi içerisinde toplamda 2 defa içermektedir.


metin = "murat vuranok"

retVal = metin.count("u")
print(retVal)  # 2
retVal = metin.count("u", 2)
print(retVal)  # 1

retVal = metin.count("u", 2, len(metin))


# verilen index değeri (dahil) ile, 3. parametrede verilen index değerine kadar olan elemanlar içerisinde arama yapacaktır.
retVal = metin.count("u", 2, 8)
print(retVal)