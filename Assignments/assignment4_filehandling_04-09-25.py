# File Handling:
# A school wants to maintain student records using a text file.
# You are required to write a Python program that performs the following file handling operations step by step:
# 1) Write Operation:
# - Create a file named students.txt.
# - Write details of students (Name, Roll Number, Marks) into the file.
# 2) Read Operation:
# - Read the content of students.txt and display it on the screen.
# 3) Rename Operation:
# - Rename the file from students.txt to student_records.txt.
# 4) Directory Operations:
# - Create a directory called SchoolData.
# - Move the renamed file student_records.txt into this directory.
# - List all files present in SchoolData to confirm the file is inside.
# 5) Delete Operation:
# - Delete the file student_records.txt from inside the directory.
# Finally, delete the SchoolData directory.
# Do create a menu taking the user input and then perform the operation

import os
import shutil
def write_operation():
    with open("students.txt", "w") as file:
        n = int(input("Enter number of students: "))
        for _ in range(n):
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            marks = input("Enter marks: ")
            file.write(f"{name}, {roll_number}, {marks}\n")
    print("Student details written to students.txt")

def read_operation():
    with open("students.txt", "r") as file:
        content = file.read()
        print("Content of students.txt:")
        print(content)

def rename_operation():
    os.rename("students.txt", "student_records.txt")
    print("File renamed to student_records.txt")

def directory_operations():
    os.makedirs("SchoolData", exist_ok=True)
    shutil.move("student_records.txt", "SchoolData/student_records.txt")
    print("File moved to SchoolData directory.")
    print("Files in SchoolData:")
    print(os.listdir("SchoolData"))

def delete_operation():
    os.remove("SchoolData/student_records.txt")
    os.rmdir("SchoolData")
    print("Deleted student_records.txt and SchoolData directory.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Write Operation")
        print("2. Read Operation")
        print("3. Rename Operation")
        print("4. Directory Operations")
        print("5. Delete Operation")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            write_operation()
        elif choice == '2':
            read_operation()
        elif choice == '3':
            rename_operation()
        elif choice == '4':
            directory_operations()
        elif choice == '5':
            delete_operation()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.") 
menu()