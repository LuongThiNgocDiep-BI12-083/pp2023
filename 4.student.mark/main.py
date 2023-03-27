import math
import numpy
import input as inp
import output

# Get input
n_students = int(input("Number of students: "))
students = []
for i in range(n_students):
    id = input(f"Student {i+1}'s ID: ")
    name = input(f"Student {i+1}'s name: ")
    dob = input(f"Student {i+1}'s date of birth: ")
    student = inp.Student(id, name, dob)
    students.append(student)

all_credit = 0
n_subjects = int(input("Number of subjects: "))
subjects = []
for i in range(n_subjects):
    id = input(f"Subject {i+1}'s ID: ")
    name = input(f"Subject {i+1}'s name: ")
    credit = int(input(f"Credit of {name}: "))
    all_credit += credit
    subject = inp.Subject(id, name, credit)
    subjects.append(subject)

# Get scores
scores = []
for student in students:
    for subject in subjects:
        score = float(input(f"Enter {subject.name} score for {student.name}: "))
        score_obj = inp.Score(student, subject, math.floor(score))
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
output.display_scores(scores)
