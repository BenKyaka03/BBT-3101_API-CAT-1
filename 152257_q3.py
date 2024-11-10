class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_expenditure(self):
        total_expenditure = sum(employee.salary for employee in self.employees)
        return total_expenditure

    def display_employees(self):
        for employee in self.employees:
            employee.display_details()


def main():
    department_name = input("Enter department name: ")
    department = Department(department_name)

    while True:
        print("\n1. Add employee")
        print("2. Display total expenditure")
        print("3. Display all employees")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)
        elif choice == "2":
            total_expenditure = department.calculate_total_expenditure()
            print(f"Total expenditure for {department_name} department: {total_expenditure}")
        elif choice == "3":
            department.display_employees()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()