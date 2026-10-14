#Encapsulate StudentProfile class

class StudentProfile:
    def __init__(
        self,
        student_name,
        score,
        skills
    ):
        self.__student_id =student_id
        self.__student_name = name 
        self.__score = score
        self.__skills = skills
    @property
    def get_student_id(self):
        return self.__student_id
    @student_name.setter
    def student_name(self, new_name):
        if name.lower().strip()!="":
            self.__name = new_name
        else:
            return "Invalid Name"
    @property
    def get_score(self):
        return self.__score
    @score.setter
    def score(self, new_score):
        if 0<new_score<100:
            self.__score = new_score
        else:
            return "Invalid score"
    @property
    def get_skills(self):
        return tuple(self.__skills)
    def add_skill(self,new_skill):
        for skill in initial_skills:
            new_skill = new_skill.strip()
            if skill not in initial_skills:
                initial_skills.append(new_skill)
                self.__skills = ", ".join(initial_skills)
                return self.__skills
            else:
                self.__skills = ", ".join(initial_skills)
                return self.__skills
    def __str__(self):
        return ("STUDENTPROFILE\n"
        f"Student ID: {self.__name}\n"
        f"Name: {self.__name}\n"
        f"Score: {self.__score}\n"
        f"Skills: {self.__skills}")
student_id = int(input("Enter student_id: "))
student_name = input("enter name:  ").strip()
initial_score = int(input("Enter initial_score : "))
skills_input = input("Enter skill input: ").strip()
new_score = int(input("enter new_score: "))
new_skill = input("Enter new_skill: ").strip()
initial_skills = [skill.strip()
            for skill in skills_input.split(",")
                if skill.strip()]
student = StudentProfile(student_id,name,new_score,initial_skills)
student.score = new_score
student.add_skill(new_skill)
print(student)