# .endswith() => metninizin parametrede gönderdiğiniz değer ile bitip bitmediğini kontrol eder.


metin = "bilge adam beşiktaş python dersleri"


sonuc = metin.endswith("eri")


if sonuc:
    print("parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmektedir")
else:
    print("parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmemektedir")


# ternary if kullanarak tek satırda mesaj veriniz.


print("parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmektedir" if sonuc else "parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmemektedir")


print(
    f"parametrede gönderdiğiniz değer 'eri' kelimesi ile bitme{'' if sonuc else 'me'}ktedir")
