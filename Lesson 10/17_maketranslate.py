# .maketrans,.translate
# mail adresi düzenleyen metot yazdık
def ClearUrl(param):
    return param.lower().replace("ç", "c").replace("ş", "s").replace(" ", "-").replace("ü", "u")


def ClearMail(param):
    return param.lower().replace("ç", "c").replace("ş", "s").replace(" ", "").replace("ü", "u")


print(ClearMail(" ahmet.şahin@hotmail.com"))
print(ClearUrl("Fakir Hercules Vücut Analiz Baskülü"))


kaynak = "şçğüıöŞÇĞÜİÖ"
hedef = "scguioSCGUIO"
metin = "bilge adam beşiktaş şubesi PYTHON DERSLERİ BAŞLADI"

table = str.maketrans(kaynak, hedef)

print(table)
metin = metin.translate(table)
print(metin)
#bilge adam besiktas subesi PYTHON DERSLERI BASLADI