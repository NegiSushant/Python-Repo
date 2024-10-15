#-----------------------Operators---------------
print("-------------Operators in python-----------")
#Airthmatic Operators
#Relational Operators
#Logical Operators
#Bitwise Operators
#Assignment Operators
#Membership Operators

#---------------if else statement --------------------
print('-----------------Conditional statement----------')
print('--------------if else statements-------------')
#login program and indentations

email = input('Enter your email: ')
password = input("Enter your password: ")

if email == 'test123@email.com' and password == '123':
    print('Welcome')
elif email == 'test123@email.com' and password != '123':
    #tell the user
    print('Incorect Password!')
    password = input('Enter password again: ')
    if password == '123':
        print('Welcome!')
    else:
        print('Beta tumse na ho payega rhn do')
elif email != 'test123@email.com' and password == '123':
    #tell users
    print("Incorect email address!")
    email = input('Enter correct email: ')
    if email == 'test123@email.com':
        print('Welcome!')
    else:
        print("Tumse na ho payega")
else:
    print('Cridential does not right')

