## x = 10
## y = 18
class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)
class Manager(Employee):
    mgr_count=0
    departament="A01"
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament=departament
        Manager.mgr_count +=1
## x=10 ; (x=)10%3=1; functia display_employee va afisa doar salariul
    def display_employee(self):
        print("Salary: ", self.salary)
## y=18 ; (y=)18/3=6; voi crea 6 obiecte din clasa Manager
man1=Manager("Ionescu Ion", 2200, "Finante")
man2=Manager("Popescu Ion", 2500, "Invatamant")
man3=Manager("Enescu Vali", 2400, "")
man4=Manager("Georgescu George", 3400, "")
man5=Manager("Popescu George", 2970, "")
man6=Manager("Popescu Pop", 3940, "")
# apelam functia display_employee pentru obiectele din clasa Manager (se va afisa doar salariu)
man1.display_employee()
man2.display_employee()
man3.display_employee()
man4.display_employee()
man5.display_employee()
man6.display_employee()
# am creat si 6 obiecte din clasa Employee
emp1=Employee("Ionescu Ion", 2200)
emp2=Employee("Popescu Ion", 2500)
emp3=Employee("Enescu Vali", 2400)
emp4=Employee("Georgescu George", 3400)
emp5=Employee("Popescu George", 2970)
emp6=Employee("Popescu Pop", 3940)
# am apelat functia display_employee pentru obiectele din clasa Employee (se va afisa numele si salariul)
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
emp4.display_employee()
emp5.display_employee()
emp6.display_employee()

print(emp1.empCount) #va afisa 12 pentru ca atat la crearea de obiecte din clasa Manager cat si de obiecte din clasa Employee se aduna 1 la variabila empCount
print(man1.mgr_count) #va afisa 6 pentru ca la crearea de obiecte din clasa Manager se aduna 1 la variabila mgr_count
