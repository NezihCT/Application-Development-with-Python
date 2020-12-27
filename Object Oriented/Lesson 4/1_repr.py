import datetime
now = datetime.datetime.now()

print(str(now))
#2020-10-25 15:43:30.067469

print(repr(now))
#datetime.datetime(2020, 10, 25, 15, 44, 20, 252068)


class Personel:
    def __init__(self, isim):
        self.FirstName = isim

    def __repr__(self):
        return "Personel('{}',{})".format(self.FirstName, self.FirstName)

    def __str__(self):
        return "{}-{}".format(self.FirstName, self.FirstName)


per = Personel("Murat")

print(str(per))
print(per)
print(repr(per))

# Murat-Murat
# Murat-Murat
# Personel('Murat', Murat)

print(per.__str__())  # son kullanıcı için çıktı teslim eder.
print(per.__repr__())  # developer için devam niteliğinde çıktı teslim eder

# Murat-Murat
# Personel('Murat',Murat)
