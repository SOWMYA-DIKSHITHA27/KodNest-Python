#complete student match processing safely
try:
    matched_skills = int(input())
    required_skills = int(input())
    match_percentage = (matched_skills/required_skills)*100
except ZeroDivisionError:
    print("Required Skills cannot be zero")
else:
    print("Match Percentage:", match_percentage)
finally:
    print("Match processing complete")