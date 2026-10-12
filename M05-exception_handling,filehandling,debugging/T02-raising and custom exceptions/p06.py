# apply custom exceptions to student data
class InvalidMarksError(Exception):
    pass
class InvalidAttendanceError(Exception):
    pass


marks = int(input("Enter student marks: "))
attendance = int(input("ENter student attendance:  "))
try:
    if marks<0 or marks>100:
        raise InvalidMarksError("Marks must be lbetween 0 and 100")
    if attendance<0 or attendance>100:
        raise InvalidAttendanceError("Attendance must be between 0 and 100")
    print("Valid student data")
except InvalidMarksError as e:
    print(e)
except InvalidAttendanceError as e:
    print(e)
