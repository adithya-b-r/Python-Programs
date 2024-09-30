class Employee:
    def __init__(self, empno, name, depname, designation, age, salary):
        self.empno = empno
        self.name = name
        self.depname = depname
        self.designation = designation
        self.age = age
        self.salary = salary
    
    def display_employee(self):
        print("Employee no.:", self.empno)
        print("Employee name:", self.name)
        print("Department name:", self.depname)
        print("Designation:", self.designation)
        print("Employee's age:", self.age)
        print("Employee's salary:", self.salary)

def main():
    n = int(input("Enter the number of employees: "))
    
    if n <= 0:
        print("At least one employee is needed. Exiting...!")
        return
    
    employees = []
    for i in range(n):
        print(f"\nEnter the details of employee {i+1}:")
        empno = int(input("Enter employee number: "))
        name = input("Enter employee name: ")
        depname = input("Enter department name: ")
        designation = input("Enter designation: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee's salary: "))
        
        employee_obj = Employee(empno, name, depname, designation, age, salary)
        employees.append(employee_obj)
    
    while True:
        empno = int(input("\nEnter the employee number you want to search: "))
        found = False
        for employee_obj in employees:
            if employee_obj.empno == empno:
                found = True
                employee_obj.display_employee()
                break
        
        if not found:
            print("Employee not found...")
        
        opt = input("\nDo you want to continue searching (Y/N)? ")
        if opt.lower() == "n":
            print("Exiting the program...")
            break

if __name__ == '__main__':
    main()