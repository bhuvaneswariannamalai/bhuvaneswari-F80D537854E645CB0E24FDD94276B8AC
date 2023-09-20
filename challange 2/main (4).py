class BankAccount:

  def __init__(self,account_number,account_holder_name,initial_balanc=0.0):
    self.__account_number =account_number
    self.__acount_holder_name = account_number_holder
    self.__account_balance = initial_balance

  def deposit(self,amount):
    if amount > 0:
      self.__accont_balance +_amount
      print("Deposite  ₹{}.New balance: ₹{}".format(account,
                                                    self.__account_balance))
    else:
      print("Invalid despoite amount.")

  def Withdrew(self,amount):
    if amount  > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw ₹{}.New balance: ₹{}".format(account,
                                              self.__accont_balance))
    else:
      print("Invalid Withdraw amount or insufficient balance.")
  def display_balance(sef):
    print("Account balance for {} (Account #{}): ₹{}".format(
          self.__account_holder_name, self.__account_number,
        self.__account_balance))


#creata an instance of the BanfAccount class
account = BankAccount(account_number="123456789",
                       account_holder_name="Hari Pabu",
                       initial_balance=500.0)

#Test desposite and withdraw functionlity
account.display_balance()
account.desposit(500.0) 
account.withdraw(200.0)
account.display()
    
    
    

