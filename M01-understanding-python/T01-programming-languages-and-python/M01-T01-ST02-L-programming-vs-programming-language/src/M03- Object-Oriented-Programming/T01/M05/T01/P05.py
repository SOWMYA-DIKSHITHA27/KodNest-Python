#process student data using else and finally
try:
    experience = int(input())
    print("Experience:", experience)
except ValueError:
    print("Invalid Experience")
finally:
    print("Student processing complete")