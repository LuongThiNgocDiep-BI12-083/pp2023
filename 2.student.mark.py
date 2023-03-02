class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        
    def __str__(self):
        return f"{self.id} - {self.name} ({self.dob})"
        
class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self.marks = {}
        
    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark
        
    def __str__(self):
        return super().__str__()

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
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        
    def add_student(self, student):
        self.students[student.id] = student
        
    def add_course(self, course):
        self.courses[course.id] = course
        
    def add_mark(self, student_id, course_id, mark):
        for student in self.students:
            if student.id == student_id:
                student.add_mark(course_id, mark)
                return
        raise ValueError("Invalid student ID")
        
    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student)
            
    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course)
            
    def show_marks(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                print(f"Marks for course: {course}")
                for student in course.students:
                    marks = student.marks.get(course_id, "N/A")
                    print(f"{student}: {marks}")
                return
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

    school = School(students, courses)

    for student in course.students:
        mark = input(f"Enter mark for {student.name}: ")
        school.add_mark(student.id, course.id, mark)

    school.list_courses()
    school.list_students()
    school.show_marks(course.id)
