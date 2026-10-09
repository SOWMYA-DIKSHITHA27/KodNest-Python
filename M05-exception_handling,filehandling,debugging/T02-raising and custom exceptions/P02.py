#validate marks with clear error message
marks= int(input("Enter marks    "))
try:
    if marks<0 or marks>100:
        raise ValueError("Marks must be between 0 and 100")
    print("Valid Marks")
except ValueError as e:
    print(e)