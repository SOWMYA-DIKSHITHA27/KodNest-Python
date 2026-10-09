#safely read student experience
try:
    student_experience = int(input())
    print("Experience:", student_experience)
except ValueError:
    print("Invalid Experience")