# python ouput
print("hello world")
print('Hello', 1, 4.5, True, False)
print('Hello', 1, 4.5, True, False, sep='||')
print('Hello', 1, 4.5, True, False, end='||')

# ------------------Data Type--------------------

#Integer
print(8)
print(1e309)

#Decimal/Float
print(8.55)
print(1.7e309)

#Boolean
print(True)
print(False)

#Text/String
print('Hello World')

#Complex
print(5+6j)

#List-> (Array in C)
print([1, 2, 3, 4, 5])

#Tupple
print((1, 2, 3, 4, 5))

#set
print({1, 2, 3, 4, 5})

#Dictionary
print({'name': 'Sushant', 'gender':'Male', 'weight':65})

#type-> to check the type
print(type([1, 2, 3, 4]))

#-------------------Variables------------------
print('----------------------Variables--------------------')
name = 'sushant'
print(name)

a = 5
b = 6
print(type(a+b))

#Dynamic typing support by python

#Dynamic binding- same name of variable holds diffirent type of data type. eg:
a = 5
print(a)
a = 'sushant'
print(a)

#-------------------Keywords and Identifiers-----------------
print("---------------Keywords and Identifiers----------------")
#KeyWords: reserved by python interpretor, (32 words in python)
#Identifiers: names create in programs

#-----------------user inputs--------------------------
print("-----------------User inputs------------------")
#static vs dynamic
#input('Entera text: ')


#--------------------------Type conversin-------------------
print('----------------Type Conversion----------------')
#implicit vs Explicit
print("----Implicit type conversion-----")
print(5+12.44)
print(type(5), type(12.44))

print("-----Explicit type conversion-------")
a = int('111')
print(type(a), a)
b = str(1111)
print(type(b), b)

 