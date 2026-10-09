#validate minimum age
try:
    user_age = int(input("Enter user age   "))
    if user_age<18:
        raise ValueError
    print("Eligible")
except ValueError:
    print("Invalid age")
