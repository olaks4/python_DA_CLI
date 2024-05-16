# Python Functions

# def greet():
#     print('Hello Matthaias, you\'re welcome to today\'s class')

# greet()

# student = input('Enter student name: ')

def greetStudent(student):
    print(f'Hello {student}, welcome to today\'s class')

greetStudent('Matthaias')
greetStudent('Babatunde')
greetStudent('Bukola')
greetStudent('Ibrahim')
greetStudent('Samuel')


# def addNumbers():
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
    
#     print(num1 + num2)
# addNumbers()

# Parameter - requirement for function to work

def addNums(num1, num2):
    result = num1 + num2
    print(result)

# Argument - the expected data
addNums(43, 3)
addNums(34, 23)


def studentProfile(name, age, location):
    print(f'{name} is {age} years old, living in {location}')

studentProfile('Bukola', 16, 'Lagos')
studentProfile('Ibrahim', 25, 'Ikoyi, Osun')
studentProfile('Matthaias', 15, 'Ipokia')

