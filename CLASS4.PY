# Control Statement 
# Conditional statement: If and else

num1 = 20
num2 = 22
res = False

# print(num1 == num2)

if (num1 == num2):
    print('Hello world')
else:
    print('Equation is not correct')

# NOT False = True
if num1 != num2:
    print('The numbers are not the same')
else:
    print('The numbers are the same')

number3 = 57
number4 = 60

if num1 != num2 and number3 >= number4:
    print('Both statements are correct')

else:
    print('Both statements in the AND are not correct')

if num1 > num2 or number3 < number4:
    print('One of the statements in the OR condition is correct')
else:
    print('None of the statements in the OR is correct')

num3 = 50
num4 = '50'
# num4 = input('Enter your number: ')

# try:
#     num4 = int(num4)
#     if num3 > num4:
#         print(f'num3 - {num3}, is greater than your input - {num4}')

#     else:
#         print('Equation no balance')

# except:
#     print(type(num4))
#     print('Your input is not a number')


if num4.isnumeric():
    num4 = int(num4)
    if num3 > num4:
        print(f'num3 - {num3}, is greater than your input - {num4}')

    else:
        print('Equation no balance')
else:
    print(f'Your input - "{num4}" is not a number')

# name = input('Enter your name: ')
name = 'Samuel'

if name == 'Parach':
    print('Your name is Parach')
elif name == 'Babatunde':
    print('Your name is Babatunde')
elif name == 'Matthaias':
    print('Your name is Matthaias')
elif name == 'Bukola':
    print('Your name is Bukola')
elif name == 'Ibrahim':
    print('Your name is Ibrahim')
elif name == 'Abeeb':
    print('Your name is Abeeb')
else:
    print('Your name is unknown')

    
student1 = {
    'Name': 'Bukola',
    'Age': 16,
    'Location': 'Oyo',
    'Profession': 'Data Analyst',
    }
student2 = {
    'Name': 'Ibrahim',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
student3 = {
    'Name': 'Abbey',
    'Age': 20,
    'Location': 'Port Harcourt',
    'Profession': 'Agba Baller',
    }
student4 = {
    'Name': 'Babatunde',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
student5 = {
    'Name': 'Matthaias',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }


student_list = [
    student1, 
    student2, 
    student3, 
    student4, 
    student5
    ]

for each_student in student_list:
    # print(each_student['Location'])
    if each_student['Location'] == 'Lagos':
        print(f'Student name is {each_student["Name"]}, student age is {each_student["Age"]}')

# result english and mathematics
# University of Ibadan requires student to have 50 or more score 
        # in both English and Mathematics to be considered for admission

# Olabisi Onabanjo University, Ago-Iwoye. requires students to have atleast 50 or more
        #  in either English or Mathematics to be considered for admission

# NOTE: must be in one condition