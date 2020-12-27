# Kullanıcı dışarıdan sipariş alınacak kitap adedi girilecek,
# birim fiyat 5 tl
# sipariş sayısı : 0 veya altı ise uyarı verdiriniz
# sipariş sayısı :  1 ile 20(dahil) ise %5 indirim uygulayınız
# sipariş sayısı : 21 ile 50(dahil) ise, %10 indirim uygulayınız
# sipariş sayısı : 51 ile 80(dahil) ise, %15 idirim uygulayınız
# sipariş sayısı : 81 ile 100(dahil) ise, %20 indirim uygulayınız
# sipariş sayısı : 100'den büyük ise, %25 indirim uygulayınız

print("""
********  Kitap Otomasyonuna Hoş Geldiniz  ******** 
*                                                 *
*                                                 *
*        Bilge Adam Kitap Satış Otomasyonu        *
*                                                 *
*                                                 *
*************************************************** 
""")

try:
    # pass
    adet = int(input("Lütfen sipariş aded giriniz : "))
    if adet > 0:

        birim_fiyat = 5
        total = 0
        discount = ""
        dolar = 7.44

        result = """
        Verilen sipariş adedi               : {}
        Adet birim fiyatı                   : {}$
        Toplam tutar                        : {}$
        Yapılan indirim oranı               : {}
        Toplam Ödemeniz Gereken Tutar       : {}$
        Türklirası olarak ödemek isterseniz : {}TL   
        """

        if adet <= 20:
            discount = "%5"
            total = (birim_fiyat * adet) * 0.95
            birinci_mahmud = "deneme"
        elif adet <= 50:
            discount = "%10"
            total = (birim_fiyat * adet) * 0.90
        elif adet <= 80:
            discount = "%15"
            total = (birim_fiyat * adet) * 0.85
        elif adet <= 100:
            discount = "%20"
            total = (birim_fiyat * adet) * 0.80
        else:
            discount = "%25"
            total = (birim_fiyat * adet) * 0.
        # print(result.format(adet, birim_fiyat,
        #                     (adet * birim_fiyat), discount, total, (total * dolar)))

        print(f"""
Verilen sipariş adedi               : {adet}
Adet birim fiyatı                   : {birim_fiyat}$
Toplam tutar                        : {(adet * birim_fiyat)}$
Yapılan indirim oranı               : {discount}
Toplam Ödemeniz Gereken Tutar       : {total}$
Türklirası olarak ödemek isterseniz : {(total * dolar)}TL   
        """)
        
    else:
        print("Minimum sipariş adedi 1'dir")


except Exception as mahmud:
    pass