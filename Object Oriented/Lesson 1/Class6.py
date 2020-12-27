# from Helpers import Clear, MathLibrary
from Employee import EmployeeService
from Employee import Employee


from Helpers import Clear
from Helpers import MathLibrary

# _cls = Clear()
# _cls.ClearScreen()

Clear.ClearScreen("clear")
result = MathLibrary.Topla("", 1, 2, 3, 4, 5)

print(result)
mail = "MURAT VURANOK@HOtMAİL.COM"

mail = Clear.ClearString(mail)
print(mail)


emp = Employee()
emp.FirstName = "murat"
emp.LastName = "VURANOK"
emp.CreateMail()

print(emp.Mail)
