n=int(input("Number of student: "))
student_id=[]
student_name=[]
student_dob=[]
for i in range(n):
    id=input("Student ID: ")
    student_id.append(id)
    name=input("Student name: ")
    student_name.append(name)
    dob=input("Student date of birth: ")
    student_dob.append(dob)

m=int(input("Number of course: "))
course_id=[]
course_name=[]
for i in range(m):
    id=input("ID course: ")
    course_id.append(id)
    name=input("Course name: ")
    course_name.append(name)

k=0
mark=[]

for i in range(m):
    for j in range(n):
        score=float(input(course_name[i]+" score of "+student_name[j]+": "))
        mark.append(score)

for i in range(n):
    print("\n"+course_id[i],course_name[i]+": ")
    for j in range(m):
        print("                     "+student_id[j],student_name[j],student_dob[j]+": "+str(+mark[k]))
        k+=1