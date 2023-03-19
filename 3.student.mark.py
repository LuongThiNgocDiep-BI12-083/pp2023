import math
import numpy

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

class Subject:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class Score:
    def __init__(self, student, subject, score):
        self.student = student
        self.subject = subject
        self.score = score

def display_scores(scores):
    students = set(score.student for score in scores)
    for student in students:
        print(f"ID: {student.id}")
        print(f"DOB: {student.dob}")
        print(f"{student.name}'s scores:")
        print(f"Subjects: {', '.join([subj.name for subj in student.subjects])}")
        print(f"GPA: {student.gpa}\n")
        for score in scores:
            if score.student == student:
                print(f"{score.subject.name}: {score.score}")
        print('\n')


# Get input
n_students = int(input("Number of students: "))
students = []
for i in range(n_students):
    id = input(f"Student {i+1}'s ID: ")
    name = input(f"Student {i+1}'s name: ")
    dob = input(f"Student {i+1}'s date of birth: ")
    student = Student(id, name, dob)
    students.append(student)

all_credit = 0
n_subjects = int(input("Number of subjects: "))
subjects = []
for i in range(n_subjects):
    id = input(f"Subject {i+1}'s ID: ")
    name = input(f"Subject {i+1}'s name: ")
    credit = int(input(f"Credit of {name}: "))
    all_credit += credit
    subject = Subject(id, name, credit)
    subjects.append(subject)

# Get scores
scores = []
for student in students:
    for subject in subjects:
        score = float(input(f"Enter {subject.name} score for {student.name}: "))
        score_obj = Score(student, subject, math.floor(score))
        scores.append(score_obj)
        student.add_subject(subject)

# Calculate GPA for each student
for student in students:
    total_score = 0
    for score in scores:
        if score.student == student:
            total_score += score.score * score.subject.credit
    gpa = total_score / all_credit
    student.set_gpa(gpa)

# Sort students by GPA in decreasing order
for i in range(len(scores)):
    for j in range(i+1,len(scores)):
        if(scores[i].score<scores[j].score):
            k=scores[i]
            scores[i]=scores[j]
            scores[j]=k

# Display scores and GPA in sorted order
display_scores(scores)