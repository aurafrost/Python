class BankAccount(object):
  balance=0
  def __init__(self,name):
    self.name=name
  def __repr__(self):
    return "Account owner: %s Balance: %.2f"%(self.name,self.balance)
  def show_balance(self):
    return "Balance: %.2f"%(self.balance)
  def deposit(self,amount):
    if(amount<=0):
      print("Invalid amount")
      return
    else:
      print("Amount to deposit %.2f"%(amount))
      self.balance+=amount
      self.show_balance()
  def withdraw(self,amount):
    if(amount<=0 or amount>self.balance):
      print("Invalid amount")
      return
    else:
      print("Amount to withdraw %.2f"%(amount))
      self.balance-=amount
      self.show_balance()
      
      
my_account=BankAccount("account")
print (my_account)
my_account.deposit(2000)
my_account.withdraw(1000)
print (my_account)
