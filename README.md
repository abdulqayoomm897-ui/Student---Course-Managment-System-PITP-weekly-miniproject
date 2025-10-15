# 🎓 Student Management System (Python OOP + Pickle)

A simple, menu-driven **Student Management System** built in **Python** using **Object-Oriented Programming (OOP)** concepts and **Pickle** for data persistence.

This project demonstrates the use of classes, objects, and file handling to manage course enrollments in a small academic setup.

---

## 🚀 Features

✅ **Courses Offered** — Displays a fixed list of 5 popular tech courses.  
✅ **Enroll Now** — Allows a student to enroll in any available course.  
✅ **View Instructor** — Displays the instructor teaching a specific course.  
✅ **Exit & Save Data** — Saves all student enrollment data in a `.pkl` file and exits safely.  

All data is **automatically saved** in a pickle file (`student_data.pkl`) and **reloaded** when the program starts again.

---

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
  - Classes & Objects
  - Methods & Attributes
  - Encapsulation
- Data Persistence using the `pickle` module
- File handling
- Menu-based program design
- Basic user input validation

---

## 🧩 Class Structure

### `Course`
| Attribute | Description |
|------------|--------------|
| `course_id` | Unique ID of the course |
| `course_name` | Name of the course |
| `instructor_name` | Name of the course instructor |

### `Student`
| Attribute | Description |
|------------|--------------|
| `student_name` | Name of the student |
| `enrolled_course` | Course object that student enrolled in |

### `StudentManagementSystem`
| Method | Description |
|--------|--------------|
| `course_offered()` | Displays available courses |
| `enroll_now()` | Enrolls a student in a course |
| `view_instructor()` | Shows instructor for a given course |
| `exit_system()` | Saves data to `.pkl` and exits |
| `menu()` | Main interactive menu for user |

---

## 🖥️ How to Run

1. Clone or download this repository.
   ```bash
   git clone https://github.com/<your-username>/student-management-system.git
   cd student-management-system
Run the Python file:

bash
Copy code
python main.py
Use the menu to:

View courses

Enroll in a course

Check instructor info

Exit (data auto-saves)

📂 Data Storage
All enrolled student records are saved in:

Copy code
student_data.pkl
This file is created automatically when you enroll students.
The data is reloaded automatically when the program starts again.

🧑‍💻 Example Interaction
java
Copy code
========== STUDENT MANAGEMENT SYSTEM ==========
1️⃣  Courses Offered
2️⃣  Enroll Now
3️⃣  View Instructor
4️⃣  Exit
===============================================
Enter your choice: 1

📘 COURSES OFFERED:
C101 - Python Programming (Instructor: Dr. Smith)
C102 - Data Science (Instructor: Prof. Alice)
C103 - Artificial Intelligence (Instructor: Dr. John)
C104 - Web Development (Instructor: Mr. Ahmed)
C105 - Database Systems (Instructor: Dr. Khan)
🛠️ Requirements
Python 3.7 or higher

No external libraries required (only built-in modules)
## Auther
Abdul Qayoom
Software Engineering
abdulqayoomm897@gmail.com
