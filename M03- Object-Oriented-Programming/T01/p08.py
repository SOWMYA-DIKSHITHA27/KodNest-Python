#protect and update a private student score
class StudentProfile:
    def __init__(
                    self,
                    name,
                    score
                ):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if 0 < new_score < 100:
            self.score = new_score
            return True
        self.score = intial_score
        return False
name = input("Enter student's name: ")
initial_score = int(input("Enter Initial Score: "))
new_score = int(input("Enter the new_score: "))
sowmya = StudentProfile('sowmya',90)
sowmya.get_score()
if sowmya.set_score(new_score):
    print("Score Updated")
    print("Name:", sowmya.name)
    print("Final Score:",sowmya.get_score() )
else:
    print("Invalid Score")
    print("Name:", name)
    print("Final Score:", initial_score)
