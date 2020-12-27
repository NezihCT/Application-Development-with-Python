# .startswith() => elinizdeki metinsel değerin, parametrede gönderdiğiniz değer ile başlayıp başlamadığınız (True veya False) olarak teslim eder.


metin = "bilge adam beşiktaş"
result = metin.startswith("bil")

print(result)


print(
    f"parametrede gönderdiğiniz değer \"bil\" anahtar kelimesi ile başlama{'' if result else 'ma'}ktadır")
