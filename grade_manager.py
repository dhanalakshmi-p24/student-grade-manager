students = [] 
def get_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        mark = float(input("Enter mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            return

        grade = get_grade(mark)

        students.append({
            "name": name,
            "mark": mark,
            "grade": grade
        })

        print("Student added successfully.")

    except ValueError:
        print("Invalid mark. Please enter a number.")
def show_results():
    if not students:
        print("No students available.")
        return

    print("\n{:<20} {:<10} {:<10}".format("Name", "Mark", "Grade"))
    print("-" * 40)

    for student in students:
        print(
            "{:<20} {:<10.2f} {:<10}".format(
                student["name"],
                student["mark"],
                student["grade"]
            )
        )

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * 40)
    print(f"Average Mark : {average:.2f}")
    print(f"Highest Mark : {highest:.2f}")
    print(f"Lowest Mark  : {lowest:.2f}")
while True:
    print("\n=== Student Grade Manager ===")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
