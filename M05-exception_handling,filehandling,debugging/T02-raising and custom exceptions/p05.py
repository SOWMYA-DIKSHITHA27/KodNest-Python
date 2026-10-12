#Apply custom Exceptions to banking rules
class InvalidAmountError(Exception):
    pass
class  InsufficientBalanceError(Exception):
    pass


balance = int(input("Enter available balance:  "))
amount=int(input("Enter amount to withdraw:  "))
try:
    if amount<=0:
        raise InvalidAmountError("Withdrawal amount must be greater than 0")
    if amount>balance:
        raise InsufficientBalanceError("Insufficient balance")
    print("Withdrawal successful")
except InvalidAmountError as e:
    print(e)
except InsufficientBalanceError as e:
    print(e)
