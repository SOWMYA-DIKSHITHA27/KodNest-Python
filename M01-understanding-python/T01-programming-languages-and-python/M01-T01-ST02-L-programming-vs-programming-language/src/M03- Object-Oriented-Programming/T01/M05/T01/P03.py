#handle multiple student profile input errors:
skills = ["python", "SQL", "Git", "HTML"]
try:
    skill_position = int(input())
    print(skills[skill_position])
except ValueError:
    print("Invalid position")
except IndexError:
    print("skill not found")