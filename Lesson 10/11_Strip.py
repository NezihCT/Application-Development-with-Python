# .strip() => metnin sağındaki ve solundaki boşlukları siler


metin = " bilge adam "
print(len(metin))  # 12

metin = metin.strip()
print(len(metin))  # 10


metin = "@bilge adam@"

# metot içerisine parametre verirseniz, gelen değer içerisindeki metnin başındaki ve sonundaki parametrede gelen değer var ise siler.

print(metin.strip('@'))  # bilge adam


metin = "@bilge adam@"
print(metin.rstrip('@'))
print(metin.lstrip('@'))
