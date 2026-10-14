#build s candidate profile with different access levels
class CandidateProfile:
    def __init__(self,name,email,score):
        self.name = name
        self._email = email
        self.__score = score
    def __str__(self):
        return (f"CANDIDATE PROFILE\n"
    f"Name: {self.name}\n"
    f"Email: {self._email}\n"
    f"Score: {self.get_score()}"
    )
    def get_email(self):
        return self._email
    def get_score(self):
        return self.__score
name = input("enter name: ")
email = input("Enter email: ")
score = input("Enter score: ")
candidate = CandidateProfile(name,email,score)
print(candidate)




