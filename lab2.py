class Emp:
    count=0
    lis = list()
    def __init__(self, fname ,lname, age, dep, sal):
        self.First_name=fname
        self.Last_name=lname
        self.Age=age
        self.Department=dep
        self.Salary=sal
        Emp.count+=1
        Emp.lis.append(self)

    def transfer(self, dep):
        self.Department=dep

    def fire(self):
        Emp.lis.remove(self)

    @classmethod
    def fire_by_name(cls, name):
        for emp in cls.lis:
            if emp.First_name == name:
                cls.lis.remove(emp)
                print(f"{name} has been fired.")
                break
        else:
            print(f"No employee found with the name {name}.")

    @classmethod
    def transfer_by_name(cls, name, dep):
        for emp in cls.lis:
            if emp.First_name == name:
                emp.Department = dep
                print(f"{name} has been transferred to {dep}.")
                break
        else:
            print(f"No employee found with the name {name}.")

    @staticmethod
    def show():
        for emp in Emp.lis:
            print(f"Name: {emp.First_name} {emp.Last_name}, Age: {emp.Age}, Department: {emp.Department}, Salary: {emp.Salary}")

    @staticmethod
    def list_emp():
        for emp in Emp.lis:
            print(f"Name: {emp.First_name} {emp.Last_name}, Age: {emp.Age}, Department: {emp.Department}, Salary: {emp.Salary}")


emp1 = Emp("John", "Doe", 30, "IT", 50000)
emp2 = Emp("Jane", "Smith", 35, "HR", 60000)

Emp.show()
print("------")
Emp.list_emp()


class manager(Emp):
    def __init__(self, fname, lname, age, dep, sal, managdep):
        super().__init__(fname, lname, age, dep, sal)
        self.Managed_department= managdep

    @staticmethod
    def show():
        for emp in Emp.lis:
            if isinstance(emp, manager):
                print(f"Name: {emp.First_name} {emp.Last_name}, Age: {emp.Age}, Department: {emp.Department}, Salary: Confidential, Managed Department: {emp.Managed_department}")
            else:
                print(f"Name: {emp.First_name} {emp.Last_name}, Age: {emp.Age}, Department: {emp.Department}, Salary: Confidential")


manager1 = manager("Mike", "Johnson", 40, "Finance", 70000, "Accounting")


print("All Employees:")
Emp.show()

print("\nAll Employees with Confidential Salary:")
manager.show()




user= input("1. Add new member\
            2. Transfer an employee\
            3. Fire an employee\
            4. Show all employees\
            5. Quit")


if user == "Add" or user == "add":
    status= input("m/e?")
    
    if status == "m":
        fname= input("Enter first name:")
        lname= input("Enter last name:")
        age= input("Enter age:")
        dep= input("Enter department:")
        sal= input("Enter salary:")
        managdep=input("Enter Managed department:")

        employee= manager(fname, lname, age, dep, sal, managdep)

        print("Successfuly saved")

    else:
        fname= input("Enter first name:")
        lname= input("Enter last name:")
        age= input("Enter age:")
        dep= input("Enter department:")
        sal= input("Enter salary:")

        employee= Emp(fname, lname, age, dep, sal)

        print("Successfuly saved")

elif user == "Transfer" or user == "transfer":
    employee_name = input("Enter the name of the employee to transfer : ")
    new_department = input("Enter the name of the department to transfer : ")
    Emp.fire_by_name(employee_name, new_department)

elif user == "fire":
    employee_name = input("Enter the name of the employee to fire: ")
    Emp.fire_by_name(employee_name)

elif user == "show all":
    
    Emp.show()

elif user == "q" or user =="quit" or user=="Quit":
    
    print("Exiting program.")





