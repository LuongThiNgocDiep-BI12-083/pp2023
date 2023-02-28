class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
    def add_marks(self, course_id, mark):
        self.marks[course_id] = mark
    def __str__(self):
        return f"{self.id} - {self.name} ({self.dob})"

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def __str__(self):
        return f"{self.id} - {self.name}"

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
    def add_student(self, student):
        self.students[student.id] = student
    def add_course(self, course):
        self.courses[course.id] = course
    def add_marks(self, student_id, course_id, mark):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            student.add_marks(course_id, mark)
        else:
            raise ValueError("Invalid student or course ID")
    def list_students(self):
        print("List of students:")
        for student in self.students.values():
            print(student)
    def list_courses(self):
        print("List of courses:")
        for course in self.courses.values():
            print(course)
    def show_marks(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            print(f"Marks for course: {course}")
            for student in course.students:
                marks = student.marks.get(course_id, "N/A")
                print(f"{student}: {marks}")
        else:
            raise ValueError("Invalid course ID")

if __name__ == '__main__':
    num_students = int(input("Enter the number of students: "))

    students = []
    for i in range(num_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        student = Student(id, name, dob)
        students.append(student)

    num_courses = int(input("Enter the number of courses: "))

    courses = []
    for i in range(num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        courses.append(course)
    for student in students:
        for course in courses:
            course.add_student(student)
        print("Select a course:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course}")
    course_index = int(input()) - 1
    course = courses[course_index]
    
    for student in course.students:
        mark = float(input(f"Enter mark for {student.name}: "))
        School.add_marks(student.id, course.id, mark)
    School.list_courses()
    School.list_students()
    School.show_marks(course.id)
