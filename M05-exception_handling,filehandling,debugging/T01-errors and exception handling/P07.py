#complete job requirement processing safely
try:
    student_experience = int(input("enter student experience:   "))
    required_experience = int(input("enter required job experience:   "))
    experience_match = (student_experience/required_experience)*100
except ValueError:
    print("Invalid experience value")
except ZeroDivisionError:
    print("required experiecnce cannot be zero")
else:
    print("Experience Match:", experience_match)
finally:
    print("Job requirement processing completed")