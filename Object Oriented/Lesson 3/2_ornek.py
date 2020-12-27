class BasePhone():
    def __init__(self):
        # protected
        self._phoneType = "Ahizeli Telefon"
        self.connectionType = None
        self.brand = None
        self.phoneType = self._phoneType

    def __str__(self):
        return f"Telefonun Bağlantı Türü : {self.connectionType}\nTelefonun Markası : {self.brand}\nTelefonun Türü : {self._phoneType}"


basePhone = BasePhone()
basePhone.connectionType = "Kablolu bağlantı"
basePhone.brand = "Alcatel"
print(basePhone)
print(basePhone.phoneType)
basePhone.phoneType = "Mobil"
print(basePhone.phoneType)


class MobilPhone(BasePhone):
    def __init__(self):
        self.hasCamera = None
        self._phoneType = "Mobil Bağlantı"


mobil = MobilPhone()
mobil.hasCamera = True
mobil.brand = "Nokia"
mobil.connectionType = "mobil connection available"


class SmartPhone(MobilPhone):
    def __init__(self):
        self.frontCamera = None
        self._phoneType = "smart phone"


smartPhone = SmartPhone()
smartPhone.brand = "apple"
smartPhone.connectionType = "5G"
smartPhone.frontCamera = True
smartPhone.hasCamera = True