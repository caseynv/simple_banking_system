import random
import sys

def landing_page():
    user = int(input("Welcome! For Staffs, Enter 1 and For Customers, Enter 2: "))
    try:
        if (user == 1):
            staff_login()
        elif (user == 2):
            customer_login()
        else:
            print("Please select 1 or 2")
            landing_page()
    except ValueError:
        print("You entered a wrong choice!")
        landing_page()

def customer_login():
    customer = int(input("Welcome! For existing customers, Enter 1 and For first-time customers, Enter 2: "))
    try:
        if (customer == 1):
            existingcustomer_login()
        elif (customer == 2):
            newcustomer_login()
        else:
            print("Please select 1 or 2")
            customer_login()
    except ValueError:
        print("You entered a wrong choice!")
        customer_login()
        

def staff_login():
    staff_user = int(input("First time? Enter 1. Existing staff? Enter 2: "))

    try:
        if (staff_user == 1):
            newstaff_login()
        elif (staff_user == 2):
            existingstaff_login()
        else:
            print("Please select 1 or 2")
            staff_login()
    except ValueError:
        print("You entered a wrong choice!")
        staff_login()

def existingstaff_login():
    existing_username = input("Welcome back! Please enter your Username: ")
    existing_password = input("Please enter your Password: ")
    
    content = 'username: ' + existing_username + " " + 'password: ' + existing_password
    credential = open('staff.txt').read()

    
    if content in credential:
        staff_dashboard()
    else:
        print("Unauthorised access!")
        staff_login()
        

    
def existingcustomer_login():
    existing_number = input("Please input your given account number: ")
    
    content = 'account number: ' + existing_number 
    credential = open('customer.txt').read()

    
    if content in credential:
        customer_dashboard()
        
    else:
        print("Unauthorised access!")
        customer_login()
    
        
    
def newstaff_login():
    new_username = input("Welcome, Guest! Please enter your preferred Username: ")
    new_password = input("Please enter your preferred Password: ")

    newstaff_content = open('staff.txt', 'a+')
    newstaff_content.write('username: ')
    newstaff_content.write(new_username)
    newstaff_content.write(' ')
    newstaff_content.write('password: ')
    newstaff_content.write(new_password)

    newstaff_content.write('\n')
    newstaff_content.close()
    staff_dashboard()

    

def newcustomer_login():
    name = input("Enter your First and Last name: ")
    email = input("Enter your Email: ")
    opening_balance = input("Enter your Opening Balance: ")
    account_number = str(random.randint(10000000000, 15000000000))
    print("Your account number is, ", account_number)

    newstaff_content = open('customer.txt', 'a+')
    newstaff_content.write('name: ')
    newstaff_content.write(name)
    newstaff_content.write(' ')
    newstaff_content.write('email: ')
    newstaff_content.write(email)
    newstaff_content.write(' ')
    newstaff_content.write('account number: ')
    newstaff_content.write(account_number)
    newstaff_content.write(' ')
    newstaff_content.write('account balance: ')
    newstaff_content.write(opening_balance)
    newstaff_content.write(' ')
                        
    newstaff_content.write('\n')
    newstaff_content.close()
    customer_dashboard()
            
 

def staff_dashboard():
    print('Welcome! \n 1: Surcharge for ATM Maintenance \n 2: Send out Emails to customer \n 3: Send out Text message to customer') 

    
def customer_dashboard():
    print('Welcome! \n 1: Debit your account \n 2: Credit your account \n 3: Change your Email \n 4: Check account balance \n 5: Check account history')

                          
landing_page()
    




