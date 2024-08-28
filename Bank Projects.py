# Create Account class with 2 attributes - balance & account no.
# Create methods for debits , credit $ printing the balance.

class Account:
    
    def __init__(self, Balance , Account):
        self.Balance = Balance
        self.Account = Account
        
    def credit(self, amount):
        self.Balance -= amount
    
    def debit(self, amount):
        self.Balance += amount
        
    def get_balance(self):
        return self.Balance
s1 = Account(200,9389826074)
print("Your Account Number is:",s1.Account , "\nAnd Your Current Balance is:",s1.Balance)
print("So Now what are you doing in your Account.\nTask are given below and press Number : 1.Credit       2.Debit")

Task = int(input("Enter The Task Nnumber :"))
if(Task == 1):
    pay = int(input("Enter The Money for Crerdit :"))
    s1.debit(pay)
elif(Task == 2):
    debit = int(input("Enter Thae Money for Debit:"))
    s1.credit(debit)

print("Now Your Current Balance is:",s1.Balance)
        