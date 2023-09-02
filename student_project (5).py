name=('shahed Adel Alamoor')
date=('2/9/2023')
print(name)
print(date)
import uuid

class Course:
    def _init_(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0

def _init_(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

def  enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0

students = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            # TODO: Check if the student_number already exists before creating a new student.
            # If not, create a new student and add them to the students list.
            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")

            new_student = Student(student_name, student_age, student_number)
            students.append(new_student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            # TODO: Find and remove the target student if they exist in the students list.
            for student in students:
                if student.student_number == student_number:
                    students.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Found")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            # TODO: Find and print the target student's details if they exist in the students list.
            for student in students:
                if student.student_number == student_number:
                    print(student.get_student_details())
                    break
            else:
                print("Student Not Found")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            # TODO: Find and print the target student's average if they exist in the students list.
            for student in students:
                if student.student_number == student_number:
                    print(f"Student Average: {student.get_student_average()}")
                    break
            else:
                print("Student Not Found")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            # TODO: Find the target student, ask the user to enter course name and mark, then add the course to the student.
            for student in students:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    try:
                        course_mark = float(input("Enter Course Mark: "))
                        student.enroll_course(course_name, course_mark)
                        print("Course Added to Student Successfully")
                    except ValueError:
                        print("Invalid Course Mark")

        elif selection == 6:
            # TODO: Implement the exit functionality.
            break

    except ValueError:
        print("Invalid selection. Please enter a valid number.")