import pickle
import os
class Course:
    def __init__(self, course_id, course_name, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor_name = instructor_name
        
class Student:
    def __init__(self, student_name, enrolled_course):
        self.student_name = student_name
        self.enrolled_course = enrolled_course


class StudentManagementSystem:
    DATA_FILE = "student_data.pkl"

    def __init__(self):
        self.students = []
        # define fixed 5 tech courses
        self.courses = [
            Course("C101", "Python Programming", "Dr. Smith"),
            Course("C102", "Data Science", "Prof. Alice"),
            Course("C103", "Artificial Intelligence", "Dr. John"),
            Course("C104", "Web Development", "Mr. Ahmed"),
            Course("C105", "Database Systems", "Dr. Khan")
        ]
        self.load_data()

    def save_data(self):
        with open(self.DATA_FILE, "wb") as f:
            pickle.dump(self.students, f)
        print("💾 Data saved successfully!")

    def load_data(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "rb") as f:
                self.students = pickle.load(f)
            print("📂 Previous enrollment data loaded.")
        else:
            print("⚙️ Starting with a fresh system.")
            
    def course_offered(self):
        print("\n📘 COURSES OFFERED:")
        for c in self.courses:
            print(f"{c.course_id} - {c.course_name} (Instructor: {c.instructor_name})")

    def enroll_now(self):
        name = input("Enter Student Name: ")
        self.course_offered()
        course_id = input("Enter Course ID to enroll: ")

        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print(" Invalid course ID.")
            return

        s = Student(name, course)
        self.students.append(s)
        print(f"✅ {name} successfully enrolled in {course.course_name}!")

    def view_instructor(self):
        self.course_offered()
        course_id = input("Enter Course ID to view its instructor: ")

        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            print(f"👨‍🏫 Instructor for {course.course_name}: {course.instructor_name}")
        else:
            print("⚠️ Course not found.")

    def exit_system(self):
        self.save_data()
        print(" Thanks for visiting us . Goodbye!")
        
    def menu(self):
        while True:
            print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
            print("1- Courses Offered")
            print("2- Enroll Now")
            print("3- View Instructor")
            print("4- Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                self.course_offered()
            elif choice == "2":
                self.enroll_now()
            elif choice == "3":
                self.view_instructor()
            elif choice == "4":
                self.exit_system()
                break
            else:
                print(" Invalid choice. Try again.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()
