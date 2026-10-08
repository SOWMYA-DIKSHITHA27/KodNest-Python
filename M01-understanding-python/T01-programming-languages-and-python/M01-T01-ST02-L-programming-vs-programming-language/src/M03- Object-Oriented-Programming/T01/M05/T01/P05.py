#process student data using else and finally
try:
    experience = int(input())
except ValueError:
    print("Invalid Experience")
else:
    print("Experience:", experience)
finally:
    print("Student processing complete")