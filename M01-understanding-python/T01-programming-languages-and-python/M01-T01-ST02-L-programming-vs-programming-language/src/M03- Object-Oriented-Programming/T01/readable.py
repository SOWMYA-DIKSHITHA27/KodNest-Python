#Add Readable Output to StudentProfilr
class StudentProfile:
    def __init__(self,student_id,name,course,experience,skills):
       self.student_id=student_id
       self.name = name
       self.course = course
       self.experience=experience
       self.skills=skills
    def __str__(self):
        return (f"STUDENT PROFILE\n"
        f"Student ID: {student_id}\n"
        f"Name: {name}\n"
        f"Course: {course}\n"
        f"Experience in Years: {experience}\n"
        f"Skills: {','.join(skills)}")
student_id=int(input().strip())
name=input().strip()
course=input().strip()
experience=int(input())
skills=input().split()

student=StudentProfile(name,name,course,experience,skills)
print(student)
