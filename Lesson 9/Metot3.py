def Metot(ad, soyad, mail, gorev, *telefon):
    print("""
    Personelin Adı                : {}
    Personelin Soyadı             : {}
    Personelin Mail Adresi        : {}
    Personelin Görevi             : {}
    Personelin Telefon Numaraları : {}
    """.format(ad, soyad, mail, gorev, " - ".join(telefon)))


Metot("murat", "vuranok", "murat.vuranok",
      "danışman", "0901234567890", "0901234567890", "0901234567890", "0901234567890")
