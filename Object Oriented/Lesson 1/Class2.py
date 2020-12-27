class Employee:
    '''
    Personel sınıfı oluşturuyoruz :) 
    '''
    FirstName = ""
    LastName = ""
    Phone = ""
    Mail = ""


emp = Employee()
emp.FirstName = "Murat"
emp.LastName = "Vuranok"
emp.Phone = "+901234567890"
emp.Mail = "murat.vuranok@bilgeadam.com"


print(emp)

# <__main__.Employee object at 0x104d9a290>
# personel'i direkt olarak print metodunda yazarsanız size heap alandaki tuttuğu yerin adresini teslim eder.

print(emp.FirstName)
