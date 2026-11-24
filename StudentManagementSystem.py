Students = []

while True:
    # Student Management System:
    print("==============================")
    print("Student Management System")
    print("==============================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Calculate Average Marks")
    print("6. Find Topper")
    print("7. Display Passed Students")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:  # Add Student

        Student_Id = int(input("Enter your Id: "))
        Student_name = input("Enter your name: ")
        Age = int(input("Enter your age: "))
        Course = input("Enter your course: ")

        Marks_Maths = int(input("Enter your Maths marks: "))
        Marks_Science = int(input("Enter your Science marks: "))
        Marks_Computer = int(input("Enter your Computer marks: "))

        student = {
            "id": Student_Id,
            "name": Student_name,
            "Age": Age,
            "Course": Course,
            "Marks_Maths": Marks_Maths,
            "Marks_Science": Marks_Science,
            "Marks_Computer": Marks_Computer
        }

        Students.append(student)

        print("Student added successfully!")

    elif choice == 2:  # Display Students

        if Students:
            for student in Students:
                print(student)
                print("-------------------------")
        else:
            print("No student data to display")

    elif choice == 3:  # Search Student

        student_name_search = input("Enter student name: ")

        found = False

        for student in Students:
            if student["name"].lower() == student_name_search.lower():
                print(student)
                found = True
                break

        if not found:
            print("No student found")

    elif choice == 4:  # Delete Student

        student_delete_id = int(input("Enter student ID to delete: "))

        deleteStudent = False

        for student in Students:
            if student["id"] == student_delete_id:
                Students.remove(student)
                print(f"Student {student_delete_id} got removed")
                deleteStudent = True
                break

        if not deleteStudent:
            print("No student found with that ID.")

    elif choice == 5:  # Average Marks

        if Students:
            for student in Students:

                total_marks = (
                    student["Marks_Maths"] +
                    student["Marks_Science"] +
                    student["Marks_Computer"]
                )

                average = total_marks / 3

                print(f"Student: {student['name']}")
                print(f"Total Marks: {total_marks}")
                print(f"Average Marks: {average:.2f}")
                print("........................")

        else:
            print("No student to calculate average.")

    elif choice == 6:  # Find Topper

        if Students:

            topper = Students[0]

            for student in Students:

                total_marks = (
                    student["Marks_Maths"] +
                    student["Marks_Science"] +
                    student["Marks_Computer"]
                )

                topper_marks = (
                    topper["Marks_Maths"] +
                    topper["Marks_Science"] +
                    topper["Marks_Computer"]
                )

                if total_marks > topper_marks:
                    topper = student

            highest_marks = (
                topper["Marks_Maths"] +
                topper["Marks_Science"] +
                topper["Marks_Computer"]
            )

            print("========== TOPPER ==========")
            print(f"Name: {topper['name']}")
            print(f"Student ID: {topper['id']}")
            print(f"Course: {topper['Course']}")
            print(f"Total Marks: {highest_marks}")
            print(f"Average: {highest_marks / 3:.2f}")

        else:
            print("No student records available.")

    elif choice == 7:  # Display Passed Students

        if Students:

            passed = False

            for student in Students:

                if (
                    student["Marks_Maths"] >= 40 and
                    student["Marks_Science"] >= 40 and
                    student["Marks_Computer"] >= 40
                ):

                    print(f"Name: {student['name']}")
                    print(f"Student ID: {student['id']}")
                    print("Status: PASSED")
                    print("-------------------------")

                    passed = True

            if not passed:
                print("No passed students found.")

        else:
            print("No student records available.")

    elif choice == 8:
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice. Please try again.")