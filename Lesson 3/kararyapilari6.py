  
# örnek : Dışarıdan kullanıcı not girişi sağlayacak
# 0  - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 - 100 => AA harf notunu aldınız uyarısı veriniz.

try:
    _not = float(input("Lütfen notunuzu giriniz : "))
    result = "Girilen {} notun karşılığı olan harf notunuz : {}"
    if _not >= 0 and _not <= 30:
        result = result.format(_not, "FF")
    elif _not > 30 and _not <= 50:
        result = result.format(_not, "DD")
    elif _not > 50 and _not <= 70:
        result = result.format(_not, "CC")
    elif _not > 70 and _not <= 84:
        result = result.format(_not, "BB")
    elif _not > 84 and _not <= 100:
        result = result.format(_not, "AA")
    else:
        result = "Lütfen 0 ile 100 arasında bir not girişi yapınız"

    print(result)
except ValueError as mahmud:
    print(mahmud)