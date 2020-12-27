# .sorted()  => dizi içerisinde yer alan elemanları A'dan Z'ye 0'dan 9'a sıralama yapar


import locale
dizi = ['a', 's', 'd', 'f', 'g', 'h', 'l', 'ş', 'ç', 'ğ', 'i', 'ğ']
#      ['a', 'd', 'f', 'g', 'h', 'i', 'l', 's', 'ç', 'ğ', 'ğ', 'ş']
# print(sorted(dizi))


# print(sorted('bilgeadambeşiktaşşubesipythondersleri'))
#['a', 'a', 'a', 'b', 'b', 'b', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'g', 'h', 'i', 'i', 'i', 'i', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'r', 'r', 's', 's', 't', 't', 'u', 'y', 'ş', 'ş', 'ş']


# alfabetik sıraya göre değil, ascii kod değerine göre sıralam yaptığından, türkçe karakterleri dizinin en sonuna ekleyecektir
#locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")  # windows için

locale.setlocale(locale.LC_ALL, locale="tr_TR")

sonuc = sorted("bilgeadambeşiktaşşubesipythondersleriç",
               key=locale.strxfrm)  # TODO : mac için araştırılacak
print(sonuc)