Students = []

while True:
    # Student Management System:
    print("==============================")
    print("Student Management System")
    print("==============================")
    
    print("1. Add Student: ")
    print("2. Display Students: ")
    print("3. Search Student: ")
    print("4. Delete Student: ")
    print("5. Calculate Average Marks")
    print("6. Find Topper")
    print("7. Display Passed Students")
    print("8. Exit")
    choice = int(input("Enter your choice for forward work: "))
    
    if choice == 1: #To Add Student
        Student_Id = int(input("Enter your Id: "))
        Student_name = input("Enter your name: ")
        Age = int(input("Enter your age: "))
        Course = input("Enter your course: ")
        Marks = int(input("Enter your Marks: "))
    
        student = {
            "id" : Student_Id,
            "name" : Student_name,
            "Age" : Age,
            "Course" : Course,
            "Marks" : Marks
        }
    
        Students.append(student)
    
    elif choice == 2: #To Display Student
        if Students:
            for student in Students:
                print(student)
        else: 
            print("No student data to display")    
    
    elif choice == 3:
        student_name_search = input("Enter student name: ")
        found = False
        for student in Students:
            if student["name"].lower() == student_name_search.lower():
                print(student)
                found = True
            if not found:
                print("No student found")

    elif choice == 4:
        student_delete_id = int(input("Enter student name to delete the detail: "))
        deleteStudent = False
        for student in Students:
            if student["id"] == student_delete_id:
                Students.remove(student)
                print(f"{student_delete_id} got remove")    
                deleteStudent = True
                break
            if not deleteStudent:
                print("No student is found with that id.")            
    
    elif choice == 8:
        print("Existing system")
        break
    else:
        print("Invalid choices")






