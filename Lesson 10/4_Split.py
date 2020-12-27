# içerisinde verilen parametreye göre,soldan sağa doğru ayırma işlemi yapar


import re
elemanlar = 'yazılım,sistem,ofis,muhasebe,teknik çizim,web grafik'
elemanlar = elemanlar.split(',')
# ['yazılım', 'sistem', 'ofis', 'muhasebe', 'teknik çizim', 'web grafik']
#print(elemanlar)

elemanlar = 'yazılım,sistem,ofis,muhasebe,teknik çizim,web grafik'
# ['yazılım,sistem,ofis,muhasebe,teknik', 'çizim,web', 'grafik']
# eğer parametre göndermezseniz, default olarak boşluklardan ayırma işlemi yapacaktir
elemanlar = elemanlar.split()
#print(elemanlar)


metin = "murat vuranok yazılım beşiktaş istanbul"

sonuc = metin.split(" ", 3)

#birinci paramerede verdiğiniz seperator değerine göre, 2. paremetrede verdiğiniz adet kadar ayırma işlemi yapacaktır.
#print(sonuc)
# ['murat', 'vuranok', 'yazılım', 'beşiktaş istanbul']

text = "bilge,adam;beşiktaş.istanbul"

a = 'Beautiful, is; better*than\nugly'
a = re.split('; |, |\*|\n', a)
print(a)