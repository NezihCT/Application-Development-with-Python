# yorum satırı
print("hello dünya")


# degisken tanimlama kurallari
# 1) degisken, ismi sayi ile baslayamaz
# 2) degisken, 2 veya fazla kelimeden olusamaz, olusacak ise, ornk
#  benim_kullaniciAdim = "kahramanmaraslimustafa"
# 3) degisken tanimlamasi yapilirken, kesinlikle tanimli kelimeler kullanilamaz
# 4) degisken adinda lutfen rica ediyorum, turkce karakter kullanmayiniz.

benim_adim = "murat vuranok"
mail_adresim = "murat.vuranok@bilgeadam.com"
adim = "murat"
soyadim = 'vuranok'

# int, strin, float
sayi = 5  # int tam sayi veri tipi
print(sayi)
print(type(sayi))

print(adim)
print(soyadim)

print(adim + " " + soyadim)  # murat vuranok
print(adim, soyadim)

fullname = adim + " " + soyadim
print("kullanıcın adı soyadı :", fullname)

x = True
y = False

print(x)
print(y)
print(type(x))

# \n bir alt satıra geç => new line
print((fullname + "\n")*5)
print(type(fullname))
 
print("""
bilge 
adam
python
yazılım
kursu
""")

print("bilge adam \"beşiktaş\" yazılım dersleri istanbul\n\
    python kursu\
    test satırı")