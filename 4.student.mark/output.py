def display_scores(scores):
    students = set(score.student for score in scores)
    for student in students:
        print(f"\nID: {student.id}")
        print(f"DOB: {student.dob}")
        print(f"{student.name}'s scores:")
        print(f"Subjects: {', '.join([subj.name for subj in student.subjects])}")
        for score in scores:
            if score.student == student:
                print(f"{score.subject.name}: {score.score}")
        print(f"GPA: {student.gpa}\n")