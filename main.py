import csv
from employee import Employee
from employee_management_system import EmployeeManagementSystem


def print_menu():
    print("\n===== Employee Management System =====")
    print("1. Print All Employees")
    print("2. Add Employee")
    print("3. Remove Employee")
    print("4. Connect Employees")
    print("5. Disconnect Employees")
    print("6. Shortest Distance Between Employees")
    print("7. Breadth First Search")
    print("8. Depth First Search")
    print("9. Minimum Spanning Tree")
    print("10. Number of Employees")
    print("11. Exit")

    return int(input("Enter your choice: "))



def main():
    system = EmployeeManagementSystem()

    # Load CSV data
    try:
        with open("data.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            employee_data = []

            for row in reader:

                if len(row) != 7:
                    print("Invalid data format in CSV file.")
                    return

                reg_num = row[0]
                age = int(row[1])
                gender = row[2]
                edu_level = row[3]
                job_title = row[4]
                years_exp = int(row[5])
                salary = int(row[6])

                emp = Employee(
                    reg_num,
                    age,
                    gender,
                    edu_level,
                    job_title,
                    years_exp,
                    salary,
                )

                employee_data.append(emp)

    except FileNotFoundError:
        print("Failed to open the file.")
        return

    for emp in employee_data:
        system.add_employee(emp)
    print("Employees loaded:", len(employee_data))
    print("Employees in system:", system.get_number_of_employees())

    while True:

        choice = print_menu()

        if choice == 1:
            system.print_employees()

        elif choice == 2:

            reg_num = input("Enter registration number: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            edu_level = input("Enter education level: ")
            job_title = input("Enter job title: ")
            years_exp = int(input("Enter years of experience: "))
            salary = int(input("Enter salary: "))

            new_employee = Employee(
                reg_num,
                age,
                gender,
                edu_level,
                job_title,
                years_exp,
                salary,
            )

            system.add_employee(new_employee)

            print("Employee added successfully!")

        elif choice == 3:

            reg_num = input(
                "Enter registration number of the employee to be removed: "
            )

            system.remove_employee(reg_num)

            print("Employee removed successfully!")

        elif choice == 4:

            reg_num1 = input(
                "Enter registration number of the first employee: "
            )

            reg_num2 = input(
                "Enter registration number of the second employee: "
            )

            weight = int(
                input("Enter weight of the connection: ")
            )

            system.connect_employees(
                reg_num1,
                reg_num2,
                weight
            )

            print("Employees connected successfully!")

        elif choice == 5:

            reg_num1 = input(
                "Enter registration number of the first employee: "
            )

            reg_num2 = input(
                "Enter registration number of the second employee: "
            )

            system.disconnect_employees(
                reg_num1,
                reg_num2
            )

            print("Employees disconnected successfully!")

        elif choice == 6:

            reg_num1 = input(
                "Enter registration number of the first employee: "
            )

            reg_num2 = input(
                "Enter registration number of the second employee: "
            )

            distance = (
                system.shortest_distance_between_employees(
                    reg_num1,
                    reg_num2
                )
            )

            print(f"\nShortest Distance: {distance}\n")

        elif choice == 7:

            reg_num = input(
                "Enter registration number of the starting employee: "
            )

            system.breadth_first_search(reg_num)

        elif choice == 8:

            reg_num = input(
                "Enter registration number of the starting employee: "
            )

            system.depth_first_search(reg_num)

        elif choice == 9:

            system.prim_mst()

        elif choice == 10:

            print(
                f"Total No. of Employees: "
                f"{system.get_number_of_employees()}"
            )

        elif choice == 11:

            print(
                "Exiting Employee Management System..."
            )

            break

        else:

            print(
                "Invalid choice! Please try again."
            )


if __name__ == "__main__":
    main()