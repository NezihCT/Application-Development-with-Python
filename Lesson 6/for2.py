from cities import sehirler

# dizi içerisinde yer alan şehirlerin içerisinde "m" harfi geçenlerin listelenmesi

for sehir in sehirler:
    if "m" in sehir.lower():
        print(sehir)  