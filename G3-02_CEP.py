import random
import string
import ast
import datetime
import fileinput
from abc import ABC, abstractmethod



#starting our program
class greeting(ABC):
  @abstractmethod
  def introduction(self):
    pass
  def names(self):
    print('HELLO WE ARE A STUDENT OF NED UNIVERSITY\nPROJECT:BANKING SYSTEM  ')
class our_names(greeting):
  def introduction(self):
    print('CS-22084 : HAFIZ AYAN AHMED')
    print('CS-22082 : MUHAMMAD HUSSAIN RAZA')
    print('CS-22085 : ROHIT DHANJEE')
  


class Account(ABC):
    customers={}
    def __init__(self):
        self.deposit = 0
        self.withdraw = 0
        self.balance = 0


    def balance_enquiry(self):
        return self.balance

    def debit(self, amount):
        self.balance -= amount
        return self.balance

    def credit(self, amount):
        self.balance += amount
        return self.balance
    def write_in_file(self,para):
        with open('customers.txt', 'a+') as cus:
            cus.write(str(para)+'\n')
   

class Checking_Account(Account):
    def __init__(self):
        super().__init__()
        self.overdraft_fees = 500
        self.credit_limit = 5000
        self.accountNo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        Account.customers['Checking Account No'] = self.accountNo
        self.customer = Customer()

    def overdraft_fee(self, overfl_amount):
      self.fee=int(input('Enter Your Amount'))
      

    def new_account_credit(self):
        while True:
            print('To Create a New Checking Account, You must to credit some amount (minimum 1000=/Rs)')
            self.f_amount = int(input("Enter your Amount: "))
            if self.f_amount <= 1000:
                print('you can not create account with this amount..')
                continue
            else:
                self.credit(self.f_amount)
                print("Thank you!!!")
                Account.customers['CheckingAccount_credit'] = self.f_amount
                break


    def Display_account_details(self):
        print("Checking Account Details")
        print("Account Number:", self.accountNo)
        print('Account Holder:', self.customer.first_name)
        print("Current Balance:", self.balance)
        print("Credit Limit:", self.credit_limit)
class With_draw(Checking_Account):
  def __init__(self):
   super().__init__()
  def withdrawMethod(self,a):
        withdraw_value = int(input('How much money do you want to withdraw? '))
        self.withdraw = withdraw_value
        if a + self.credit_limit >= self.withdraw:
            if a >= self.withdraw:
                a -= self.withdraw
                Account.customers['Checking Account withdrawl']=a
                print(f"Your Current Balance is {a}")
                return a
            else:
                overdraft_amount = self.withdraw - a
                a = 0
                a -= self.overdraft_fees
                print(f"Overdraft fee charged: {self.overdraft_fees}")
                print(f"Remaining credit limit: {self.credit_limit - overdraft_amount}")
                print(f"")
        else:
            print("Exceeded credit limit.")
        
class Saving_Account(Account):
    def __init__(self):
        super().__init__()
        self.interest_rate = 4
        self.accountNo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        Account.customers['Saving Account Number'] = self.accountNo
        self.calculate_interest_rate()
        self.customer = Customer()

    def calculate_interest_rate(self):
        interest = self.balance * (self.interest_rate / 100)
        self.credit(interest)
        Account.customers['Saving Account Interest Balance']=interest

    def sav_debit(self):
        i = int(input("How much money do you want to debit from Your Account"))
        self.debit(i)
        Account.customers['Saving Account debit']=i
    def sav_credit(self):
        c = int(input("How much money do you want to credit in Your Account"))
        self.credit(c)
        Account.customers['Saving Account credit']=c

    def new_account_credit(self):
        while True:
            print('To Create a New Saving Account, You must to credit some amount (minimum 1000=/Rs)')
            f_amount = int(input("Enter your Amount: "))
            if f_amount <= 1000:
                print('you can not create account with this amount..')
                continue
            else:
                self.credit(f_amount)
                print("Thank you!!!")
                Account.customers['SavingAccount_credit'] = f_amount
                # return f_amount
                break
    def Display_Saving_details(self):
        print("Saving Account Details")
        print("Account Number:", self.accountNo)
        print(f'Account Holder: {self.customer.first_name} {self.customer.last_name}')
        print("Current Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)

class Loan(Account):
    def __init__(self):
        self.principal_amount = 0
        self.interest_rate = 5
        self.loan_duration = 6
        super().__init__()
    
    def loan_method(self):
        print('ENTER 1 IF YOU HAVE AN ACCOUNT IN A BANK')
        
        loan1 = int(input('ENTER YOUR CHOICE: '))
            
        if loan1 == 1:
                loan_input = int(input("ENTER YOUR AMOUNT: "))
                self.principal_amount = loan_input
                self.debit_interest()
        else:
            print('YOU DO NOT HAVE AN ACCOUNT IN THE BANK. PLEASE CREATE YOUR ACCOUNT')
          
    
    def calculate_total_payment(self):
        total_interest = self.principal_amount * self.interest_rate * self.loan_duration
        total_payment = self.principal_amount + total_interest
        print('YOU HAVE TO PAY:', total_payment)
        return total_payment
    
    def calculate_monthly_payment(self):
        print('YOUR LOAN DURATION IS 6 MONTHS')
        total_payment = self.calculate_total_payment()
        monthly_payment = total_payment / self.loan_duration
        return monthly_payment
    
    def debit_interest(self):
        interest = self.calculate_monthly_payment()
        self.debit(interest)
        Account.customers['Loan Debit:'] = interest

class Customer(Account):
  


    def __init__(self):
        super().__init__()
        self.username = ""
        self.password = ""
        self.first_name = ''
        self.last_name = ""
        self.address = ""
        self.account_type = ''
        self.phone_number = 0
        self.accountNo = 0
        self.customer_dict = {}

    def new_customer(self):
        self.username = input("Enter Your Username: ")
        Account.customers['username'] = self.username
        self.password = (input('Enter Password: '))
        Account.customers['Password'] = self.password
        self.first_name = input('Now,\nEnter Your First Name: ')
        Account.customers['firstname'] = self.first_name
        self.last_name = input('Enter Your Last Name: ')
        Account.customers['lastname'] = self.last_name
        self.address = input('Enter Your Address: ')
        Account.customers['address'] = self.address
        self.phone_number = int(input('Enter Your Phone Number: '))
        Account.customers['phone_number'] = self.phone_number
        self.account_typ()
    def account_typ(self):
      self.account_type = input('NOW YOU CREATE A SAVING AND CHECKING ACCOUNT \n. PLEASE ENTER 1 FOR CHECKING ACCOUNT AND ENTER 2 FOR SAVING ACCOUNT \n.ENTER YOUR CHOICE: ')

      if self.account_type == '1':
        Account.customers['AccountType'] = ['Checking Account']  # Initialize the 'AccountType' key with a list
        a1 = Checking_Account()
        a1.new_account_credit()
        a1.Display_account_details()
      elif self.account_type == "2":
        
        if 'AccountType' not in Account.customers:
            Account.customers['AccountType'] = []  # Initialize the 'AccountType' key with an empty list if it doesn't exist
        Account.customers['AccountType'].append('Saving Account')
        a2 = Saving_Account()
        a2.new_account_credit()
        a2.Display_Saving_details()
        
         



class Sign_in(Account):
  
  while True:
    
    def __init__(self):
        super().__init__()

    def sign_in(self):
        self.read = open('customers.txt', 'r')
        self.data = self.read.read()

        self.name = input('Enter Name: ')
        self.password = input('Enter your Password: ')

        self.individual_dictionaries = self.data.split('\n')
        found_user = None
        for dictionary_str in self.individual_dictionaries:
            dictionary = ast.literal_eval(dictionary_str)
            if self.name in dictionary.get('username', '') and self.password in dictionary.get('Password', ''):
                found_user = dictionary
                break

        if found_user:
            print('CONGRATULATIONS, YOU SUCCESSFULLY LOGGED IN')
            print(f'YOUR NAME: {found_user.get("firstname")} {found_user.get("lastname")}')
            print(f"PHONE NUMBER:{found_user.get('phone_number')}")
            print(f'YOUR ACCOUNTS:{found_user.get("AccountType")}')
       
            if len(found_user.get('AccountType')) ==2:
              print('ENTER 1 FOR CHECKING ACCOUNT ') 
              print('Enter 2 FOR SAVING ACCOUNT')
              ac=int(input('ENTER YOUR CHOICE:  '))
              if ac == 1:
                print(f"YOUR CHECKING ACCOUNT BALANCE IS: {found_user.get('CheckingAccount_credit')}")
                print("Now You Can Perform Banking Operations")
                print('ENTER 1 FOR BALANCE ENQUIRY')
                print('ENTER 2 FOR CREDIT')
                print('ENTER 3 FOR DEBIT')
                print('ENTER 4 FOR WITHDRAW')
                choice = int(input('Enter the number corresponding to the operation you want to perform: '))
                if choice == 1:
                  self.balance=found_user.get('CheckingAccount_credit', 0)
                  print(f"Your total balance is {self.balance}")
                elif choice == 2:
                    amount = int(input("Enter the amount to credit: "))
                    self.credit(amount)
                    with open('customers.txt', 'r') as file:
                      contents = file.readlines()
                      with open('customers.txt', 'w') as cus:
                            cus.write('')
                      
                      for line in contents:
                        customer_dict = ast.literal_eval(line.strip())
                        if customer_dict['username']==self.name :
                          customer_dict["CheckingAccount_credit"] += int(amount)
                          with open('customers.txt', 'a+') as cus:
                            cus.write(str(customer_dict) + '\n')  
                        else:
                          with open('customers.txt', 'a+') as cus:
                            cus.write(str(customer_dict) + '\n')


                elif choice == 3:
                    amount = int(input("Enter the amount to debit: "))
                    self.debit(amount)
                elif choice == 4:
                  obj=With_draw()
                  withdraw_amount = found_user.get('CheckingAccount_credit')
                  a1=obj.withdrawMethod(withdraw_amount)
                  found_user['CheckingAccount_credit']=a1
              if ac ==2:
                print(f"YOUR SAVING ACCOUNT BALANCE IS: {found_user.get('SavingAccount_credit')}")
                print("Now You Can Perform Banking Operations")
                print('ENTER 1 FOR BALANCE ENQUIRY')
                print('ENTER 2 FOR CREDIT')
                print('ENTER 3 FOR DEBIT')
                print('ENTER 4 FOR WITHDRAW')
                choice = int(input('Enter the number corresponding to the operation you want to perform: '))
    
                if choice == 1:
                  self.balance=found_user.get(found_user.get('SavingAccount_credit', 0))
                  print(f"Your total balance is {self.balance}")
                elif choice == 2:
                    amount = int(input("Enter the amount to credit: "))
                    self.credit(amount)
                    with open('customers.txt', 'r') as file:
                      contents = file.readlines()
                      with open('customers.txt', 'w') as cus:
                            cus.write('')
                      
                      for line in contents:
                        customer_dict = ast.literal_eval(line.strip())
                        if customer_dict['username']==self.name :
                          customer_dict["SavingAccount_credit"] += int(amount)
                          with open('customers.txt', 'a+') as cus:
                            cus.write(str(customer_dict) + '\n')  
                        else:
                          with open('customers.txt', 'a+') as cus:
                            cus.write(str(customer_dict) + '\n')
                elif choice == 3:
                    amount = int(input("Enter the amount to debit: "))
                    self.debit(amount)
                elif choice == 4:
                  obj=With_draw()
                  withdraw_amount = found_user.get('SavingAccount_credit')
                  a1=obj.withdrawMethod(withdraw_amount)
                  found_user['SavingAccount_credit']=a1
        else:
            print('Invalid credentials or user not found.')

        self.read.close()
        print('THANKS FOR COMING')

    break  
class Transaction(Sign_in):
  def transation_method(self):
    updatedCustomerDict = {}
    self.name=input('ENTER USERNAME:  ')
    self.amount=input('ENTER AMOUNT:   ')
    with open('customers.txt', 'r') as file:
      contents = file.readlines()
      with open('customers.txt', 'w') as cus:
            cus.write('')
      
      for line in contents:
        customer_dict = ast.literal_eval(line.strip())
        if self.name == customer_dict['username'] :
          customer_dict["CheckingAccount_credit"] += int(self.amount)
          with open('customers.txt', 'a+') as cus:
            cus.write(str(customer_dict) + '\n')  
        else:
          with open('customers.txt', 'a+') as cus:
            cus.write(str(customer_dict) + '\n')

     
      with open('transaction.txt', 'a+') as cus:
        cus.write(str({'USERNAME':self.name,' Credit_Amount':self.amount}) + '\n') 
        print('HAVE A NICE DAY')
class Admin:
  #username of admin is nedcis@gmail.com
  #password of admin is cisd
  def admin(self):
    print('WELCOME IS ADMIN INTERFACE')
    

    self.name = input('ENTER USER NAME FOR ADMIN:     ')
    self.password = input('ENTER A PASSWORD FOR ADMIN:     ')
    
    if self.name =='nedcis@gmail.com' and self.password =='cisd':
      print('PRESS 1 FOR RECORD OF CUSTOMER')
      print('PRESS 2 FOR TRANSACTION SLIP')
      record = input('ENTER YOUR CHOICE: ')
      if record == '1':
        with open('customers.txt', 'r') as file:
          contents = file.readlines()
        for line in contents:
          customer_dict = ast.literal_eval(line.strip())
          for key, value in customer_dict.items():
            print(key, ":", value)
            print('')
            
          print('')
          print('--------------------------------------------------------------------------------------')
          print('')


      if record =='2':
        r1=open('transaction.txt','r')
        print(r1.read())

       
    else:
      print('PLEASE ENTER COORECT USERNAME AND PASSWORD FOR ADMIN')
        
class interface(Account):
    def welcome(self):
        while True:
            print('WELCOME IN USER INTERFACE')
          
            chi = input('Select Appropriate Options: \n1. Create An Account.\n2. Sign In in your Account.\n3. '
                        'Transaction.\n4. Take Loan.\nEnter Your Choice: ')
          
            if chi == '1':
                create = Customer()
                create.new_customer()
                counter = 1
            
                while True:
                    counter += 1
                    more = input('NOW CREATE OTHER OCCOUNT \n PRESS THE RESPECTIVE KEY \n FIRST ENTER Y: ')
                    if (counter != 2) and (more == 'Y' or 'y'):
                        create.account_typ()
                        print("YOU CAN CREATE ONLY TWO ACCOUNTS AND YOU DID IT>>")
                        self.write_in_file(Account.customers)
                        break
            
            if chi=='2':
              s=Sign_in()
              s.sign_in()
            if chi == '3':
              obj=Transaction()
              obj.transation_method()
            if chi=='4':
              obj = Loan()
              obj.loan_method()
              print('-----------------------------------------------------')

            break 

        obj=main_interface()
        obj.start()
        print('')

class main_interface():
  def start(self):
    try:
      print('')
      print('WELCOME TO BANK AL HABIB')
      print('-------------------------------------------------------------------')
      print('NOW YOU ENTER A KEY FOR ADMIN OR CUSTOMER>>>>>>>>')
      self.choice=input('PRESS U FOR ADMIN AND PRESS C FOR CUSTOMER:   ')
      
      if self.choice =='U' or self.choice=='u':
        a=Admin()
        a.admin()
     
      elif self.choice =='C' or self.choice=='c':
        i=interface()
        i.welcome()
      else:
        print('PLEASE ENTER A CORRECT INFORMATION OR KEY')
    except Exception as e:
      print('An error occurred:', str(e))

#driver code
C=our_names()
C.introduction()
C.names()

obj=main_interface()
obj.start()

