#Handle skill processing errors
try:
    matched_skills = int(input("enter matched_skills   "))
    required_skills = int(input("enter required_skills   "))
    match_percentage = (matched_skills/required_skills)*100
    print("Match Percentage:", match_percentage)
except ValueError:
    print("Invalid numeric input")
except ZeroDivisionError:
    print("skill count is zero")

