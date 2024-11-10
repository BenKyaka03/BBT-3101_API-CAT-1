class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for assignment, grade in self.assignments.items():
            print(f"- {assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned grade {grade} to {student.name} for {assignment_name}")
                return
        print("Student not found")

    def display_students_and_grades(self):
        print(f"Students and grades for {self.course_name}:")
        for student in self.students:
            student.display_grades()
            print()

def main():
    instructor = Instructor("John Doe", "CS 101")

    print("Welcome to the course management system!")
    while True:
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display students and grades")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)
            print(f"Added student {name} with ID {student_id}")
        elif choice == "2":
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)
        elif choice == "3":
            instructor.display_students_and_grades()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()