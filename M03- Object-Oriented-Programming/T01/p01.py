#update a Student's Experience and Skills
class StudentProfile:
    def __init__(self,name,experience,skills):
        self.name=name
        self.experience=experience
        self.skills=skills
    def update_experience(self,new_experience):
        self.experience=new_experience
    def add_skill(self,new_skill):
        self.skills.append(new_skill)
        self.skills=', '.join(self.skills)
name=input()
experience=int(input())
skills=input().split()
new_experience=int(input())
new_skill=input()
student=StudentProfile(name,experience,skills)
student.update_experience(new_experience)
student.add_skill(new_skill)
print(f"Name: {student.name}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {student.skills}")