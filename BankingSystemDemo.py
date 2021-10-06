import random
import sys

def landing_page():
    user = int(input("Welcome! For Staffs, Enter 1 and For Customers, Enter 2: , to close the app enter 3: "))
    try:
        if (user == 1):
            staff_login()
        elif (user == 2):
            customer_login()
        elif(user ==3):
            close_app(user)
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
        with open('staff_session.txt', 'w+') as staff_session:
            staff_session.write(content)
            
        print('Welcome {0}'.format(existing_username))
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

    print('Welcome {0}'.format(new_username))
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
    print('Welcome {0}'.format(name))
   
    customer_dashboard()
            
 

def staff_dashboard():
    
    user_input = int(input('1: Surcharge for ATM Maintenance \n 2: Send out Emails to customer \n \n Choice: '))
    
    try:
        if user_input == 1:
            surcharge_fee()
        elif user_input == 2:
            emails_out()
        else:
            print("Invalid entry!")
            staff_dashboard()
    except ValueError:
        print("Check your entry and try again!")
        staff_dashboard()
    
def customer_dashboard():
    user_input = int(input('1: Debit your account \n 2: Credit your account \n 3: Change your Email \n 4: Check account details \n \n Choice: '))
    try:
        if user_input == 1:
            debit_account()
        elif user_input == 2:
            credit_account()
        elif user_input == 3:
            change_email()
        elif user_input == 4:
            check_account()
        else:
            print("Invalid entry!")
            customer_dashboard()
    except ValueError:
        print("Check your entry and try again!")
        customer_dashboard()


def close_app(user):
    print("Thanks for banking with us! Have a wonderful day ahead!")
    sys.exit()

def debit_account():
    amount_ = int(input('Enter the amount you would like to withdraw: '))

    opening_balance = int(input("Enter your previous amount: "))

    new_balance = str(opening_balance - amount_)
    prev_balance = str(opening_balance)
    
    content = 'account balance: ' + prev_balance
    with open('customer.txt', 'r+') as d:
    
        detail = d.read()

        if content in detail:
            details = detail.replace(prev_balance, new_balance)
            d.write(details)
            
            print('Success! Thank you for banking with us')
            sys.exit()
        else:
            print('Error! Check your details and try again')
            debit_account()

def credit_account():
    mount_ = int(input('Enter the amount you would like to withdraw: '))

    opening_balance = int(input("Enter your previous amount: "))

    new_balance = str(opening_balance + amount_)
    prev_balance = str(opening_balance)
    
    content = 'account balance: ' + prev_balance
    with open('customer.txt', 'r+') as d:
    
        detail = d.read()

        if content in detail:
            details = detail.replace(prev_balance, new_balance)
            d.write(details)
            
            print('Success! Thank you for banking with us')
            sys.exit()
        
        else:
            print('Error! Check your details and try again')
            credit_account()

def change_email():
    new_email = input('Enter the new email you would like to use: ')

    old_email = input("Enter your registered email: ")
    
    content = 'email: ' + old_email
    
    with open('customer.txt', 'r+') as d:
    
        detail = d.read()

        if content in detail:
            details = detail.replace(old_email, new_email)
            d.write(details)
            
            print('Success! Thank you for banking with us')
            sys.exit()
            
        else:
            print('Error! Check your details and try again')

            customer_dashboard()

def check_account():
    account_number = input('Please enter your account number: ')
    
    content = 'account number: ' + account_number
    detail = open('customer.txt').read()

    if content in detail:
        for lines in readline():
            print(lines)
            sys.exit()
        
    else:
        print('Error! Check your account number and try again')
        credit_account()

def surcharge_fee():
    debit_account()

def emails_out():
    check_account()
                          
landing_page()
