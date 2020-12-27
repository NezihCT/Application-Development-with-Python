from Employee import Calisan


class Yonetici(Calisan):  # yönetici sınıfına çalışan sınıfını miras veriyoruz
    def __init__(self, firstname, lastname, salary, department, age=18, employeeCount=0):
        self.FirstName = firstname
        self.LastName = lastname
        self.Salary = salary
        self.Department = department
        self.Age = age
        self.EmployeeCount = int(employeeCount)

    def BilgiGoster(self):
        # super() miras aldığınız sınıfın değerlerini teslim eder.
        # Calisan sınıfının içerisindeki metodu çalıştırıp, gelen değeri teslim alıyoruz.
        info = super().BilgiGoster()
        return f"{info }\nYöneticinin Toplam Çalışan Sayısı : {self.EmployeeCount}"

    def Print_Base(self):
        for base in self.__class__.__bases__:
            print("Bu sınıfın miras adlığı sınıf :", base.__name__)

    def __str__(self):
        info = super().__str__()
        return f"{info} Yöneticidir"


yonetici = Yonetici("ahmet", "şahin", 10000, "yazılım", 90, 10)

info = yonetici.BilgiGoster()
print(info)
# TypeError: __init__() missing 4 required positional arguments: 'firstname', 'lastname', 'salary', and 'department'


yonetici.Print_Base()
print(yonetici)