#Update a Student's Experience and Skills
class StudentProfile:
    def __init__(self,name,experience,skills):
        self.name=name
        self.experience=experience
        self.skills=skills

    def update_experience(self,new_experience):
        self.experience=new_experience

    def add_skill(self,new_skill):
        self.skills.append(new_skill)

name=input().strip()
experience=int(input().strip())
skills= input().split()
new_experience=int(input().strip())
new_skill=input().strip()
student=StudentProfile(name,experience,skills)
updated_experience=student.update_experience(new_experience)
updated_skills=student.add_skill(new_skill)
print("Name:", name)
print("Experience in Years:", new_experience)
print("Skills:", ','.join(skills))