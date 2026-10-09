#create an exception for insufficient balance
class InsufficientBalanceError(Exception):
    pass
amount = int(input("Enter amount to withdraw   "))
balance = int(input("Enter available balance   "))
try:
         if amount>balance:
             raise InsufficientBalanceError("Insufficient balance")
         print("Withdrawal allowed")
except InsufficientBalanceError as e:
              print(e)