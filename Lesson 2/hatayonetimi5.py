try:
    # db connection open
    sayi = int(input("Lütfen sayı giriniz : "))
    # connection error
    print("Tebrikler bro")
    # - db connection close -
except:
    print("vazgeçtim")
    # - db connection close -
finally:
    print("her durumda bir defa tetiklenir")
    # db connection close
    # her iki durumda da yapılması gereken işlemleriniz var ise, 
    # bunu finally içerisinde yazmanız kod tekrarını engelleyecektir.