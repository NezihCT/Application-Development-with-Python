class Calisan():
    def __init__(self, firstname, lastname, salary, department, age=18):
        self.FirstName = firstname
        self.LastName = lastname
        self.Salary = salary
        self.Department = department
        self.Age = age

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    def BilgiGoster(self):
        return f"Personelin Adı : {self.FirstName}\nPersonelin Soyadı : {self.LastName}\nPersonelin Maaşı : {self.Salary}\nPersonelin Departmanı : {self.Department}\nPersonelin Yaşı : {self.Age}"

    def ZamYap(self, yapilanZam):
        print("Çalışanın Maaşına zam yapıldı")
        maas = self.Salary
        self.Salary += yapilanZam
        print(
            f"{self} Adlı personelin {maas} olan maaşı {self.Salary} olarak düzenlendi")

    def DepartmanGuncelle(self, yeniDepartman):
        print("Çalışanın Depertman Bilgisi Güncelleniyor")
        departman = self.Department
        self.Departman = yeniDepartman
        print(
            f"{self} adlı personelin {departman} olan birimi {self.Departman} olarak güncellendi")


# personel = Calisan("murat", "vuranok", 123, "yazılım", 90)
# print(personel)
# personel.BilgiGoster()
# personel.ZamYap(10000)
# print(personel.BilgiGoster())
# personel.DepartmanGuncelle("sistem")