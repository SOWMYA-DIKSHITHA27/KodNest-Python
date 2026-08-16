class StudentProfile:
    def __init__(self,student_id,student_name,course,score=0.00,skills=None,is_placed=False):
        self.student_id=student_id
        self.student_name=student_name
        self.course=course
        self.score=score
        self.is_placed=is_placed
        self.skills=[] if skills is None else list(skills)
    def __str__(self):
        skills_text=(",".join(self.skills))if self.skills else "Not Added"
        placement_status=("Placed" if self.is_placed else "Not Placed")
        return (
            f"student id: {self.student_id}\n"
            f"Student Name: {self.student_name}\n"
            f"Course: {self.course}\n"
            f"score: {self.score}\n"
            f"skills: {self.skills}\n"
            f"Placement Status: {self.is_placed}\n"
        )
student=StudentProfile(101,"Sowmya","Python",80.0,["Python","SQL","Java"],True)
print(student)