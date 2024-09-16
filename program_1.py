'''Create a program that manages a list of student names, allowing the user to add, remove, and display the list.'''

students = []

def add_student():
    name = input("Enter the student's name to add: ")
    students.append(name)
    print(f"{name} has been added.")

def remove_student():
    name = input("Enter the student's name to remove: ")
    if name in students:
        students.remove(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found in the list.")

def display_students():
    if students:
        print("Student List:")
        for i, name in enumerate(students, 1):
            print(f"{i}. {name}")
    else:
        print("The student list is empty.")

# Main 
while True:
    print("\nChoose an option:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Display student list")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        remove_student()
    elif choice == '3':
        display_students()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
