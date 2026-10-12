#apply exception validation to user registration
class InvalidAgeError(Exception):
    pass
class InvalidPasswordError(Exception):
    pass

age = int(input("Enter user age:  "))
password = input("Enter password:  ")
try:
    if age<18:
        raise InvalidAgeError("Age must be greater than or equal to 18")
    if len(password)<6:
        raise InvalidPasswordError("length of password should be at least 6")
    print("Registration successful")
except InvalidAgeError as e:
    print(e)
except InvalidPasswordError as e:
    print(e)