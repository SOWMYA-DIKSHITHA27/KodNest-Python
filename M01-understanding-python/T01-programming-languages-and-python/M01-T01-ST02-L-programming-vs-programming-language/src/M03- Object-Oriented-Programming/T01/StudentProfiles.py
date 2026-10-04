#create two student profiles with independent data
class StudentProfile:
    def __init__(self,student_id,name,course):
        self.student_id=student_id
        self.name=name
        self.course=course
first_id=int(input())
first_name=input()
first_course=input()
second_id=int(input())
second_name=input()
second_course=input()
first_student=StudentProfile(first_id,first_name,first_course)
second_student=StudentProfile(second_id,second_name,second_course)
print("Student 1")
print(f"ID: {first_student.student_id}")
print(f"Name: {first_student.name}")
print(f"Course: {first_student.course}")
print("Student 2")
print(f"ID: {second_student.student_id}")
print(f"Name: {second_student.name}")
print(f"Course: {second_student.course}")

