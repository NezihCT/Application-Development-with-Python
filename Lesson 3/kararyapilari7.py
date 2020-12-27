try:
    _not = int(input("Lütfen notunuzu giriniz : "))
    if(_not >= 0 and _not <= 100):
        result = "harf notunuz : "
        if _not <= 30:
            result += "FF"
        elif _not <= 50:
            result += "DD"
        elif _not <= 75:
            result += "CC"
        elif _not <= 85:
            result += "BB"
        else:
            result += "AA"
        print(result)
    else:
        print("Geçersiz not girişi")
except ValueError as mahmud:
    print("ne diyem, mahmud mu diyem")