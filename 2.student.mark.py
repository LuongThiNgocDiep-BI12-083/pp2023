class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.id = id
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Score:
    def __init__(self, student, subject, score):
        self.student = student
        self.subject = subject
        self.score = score

def display_scores(scores):
    for score in scores:
        print(f"{score.student.name}'s score for {score.subject.name}: {score.score}")

# Get input
n_students = int(input("Number of students: "))
students = []
for i in range(n_students):
    id = input(f"Student {i+1}'s ID: ")
    name = input(f"Student {i+1}'s name: ")
    dob = input(f"Student {i+1}'s date of birth: ")
    student = Student(id, name, dob)
    students.append(student)

n_subjects = int(input("Number of subjects: "))
subjects = []
for i in range(n_subjects):
    id = input(f"Subject {i+1}'s ID: ")
    name = input(f"Subject {i+1}'s name: ")
    subject = Subject(id, name)
    subjects.append(subject)

# Get scores
scores = []
for student in students:
    for subject in subjects:
        score = float(input(f"Enter {subject.name} score for {student.name}: "))
        score_obj = Score(student, subject, score)
        scores.append(score_obj)
        student.add_subject(subject)

# Display scores
display_scores(scores)