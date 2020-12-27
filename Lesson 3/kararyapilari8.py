# -----

# Kullanıcı dışarıdan ürün adı girecek,
# domates - biber - patlıcan  => sebze reyonu
# şampuan - parfüm - deodorant => kozmetik reyonu
# cep telefonu -  televizyon - bilgisayar - kulaklık => teknoloji reyonu

# farklı bir ürün girerse, bu ürün bizde bulunmamaktadır uyarısı veriniz.

urun = input("Lütfen ürün adı girini : ").lower().replace(
    " ", "").replace("ü", "u").replace("ş", "s").replace("ı", "i")
_len = 10
if len(urun) > _len:
    result = "Aradığınız {}, {} reyonundadır!"
    if urun == "domates" or urun == "biber" or urun == "patlican":
        result = result.format(urun, "sebze")
    elif urun == "sampuan" or urun == "parfum" or urun == "deodorant":
        result = result.format(urun, "kozmetik")
    elif urun == "ceptelefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklik":
        result = result.format(urun, "teknoloji")
    else:
        result = "Geçersiz ürün adı"
    print(result)
else:
    print(f"Lütfen minimum {_len} karakterli bir ürün adı giriniz")
