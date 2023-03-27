class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.id = id
        self.subjects = []
        self.gpa = 0

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_gpa(self, gpa):
        self.gpa = gpa