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