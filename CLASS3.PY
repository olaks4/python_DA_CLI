# Loop a list

student_list = [
    'Ibrahim', 
    'Matthias', 
    'Bukola', 
    'Babatunde', 
    'Abeeb'
    ]
age_list = [ 21, 13, 46, 7]

# For Loop
# Iteration

# print(student_list.index('Bukola'))
# print('1. Hello, good morning', student_list[0])
# print('2. Hello, good morning', student_list[1])
# print('3. Hello, good morning', student_list[2])
# print('4. Hello, good morning', student_list[3])
# print('5. Hello, good morning', student_list[4])

for each_student in student_list:
    pos = student_list.index(each_student)
    print(f'{pos+1} Hello, good morning {each_student}')
    print('')

print(each_student)
    
# Python collections
# List, Tuple, Set, Dict
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. It comes in pairs (Key and Value)

student_in_tupleclass = ('Sam', 'Matthaias', 'Bukola', 'Babatunde')

print(student_in_tupleclass[1])

for i in student_in_tupleclass:
    print(i)
    
    
student_in_setclass = {'Abeeb', 'Ibrahim', 'Babatunde', 'Bukola', 'Matthaias'}

print(student_in_setclass)

for i in student_in_setclass:
    print(i)
    
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
print('')
print('')

print(student1['Name'], student1['Age'], student1['Location'], student1['Profession'])
print(student2['Name'], student2['Age'], student2['Location'], student2['Profession'])
print(student3['Name'], student3['Age'], student3['Location'], student3['Profession'])
print(student4['Name'], student4['Age'], student4['Location'], student4['Profession'])
print(student5['Name'], student5['Age'], student5['Location'], student5['Profession'])

print(student1)

student1['Friends'] = ['Samuel', 'Matthaias', 'Abeeb']
student1['Age'] = 65
print(student1)

for each_key in student1:
    print(student1[each_key])
    
student_list = [
    student1, 
    student2, 
    student3, 
    student4, 
    student5
    ]

print(student_list)

print('')
print('')
for each_student in student_list:
    print(each_student)
    
student6_name = input('Enter student name: ')
student6_age = input('Enter student age: ')
student6_location = input('Enter student location: ')
student6_profession = input('Enter student profession: ')

student6 = {
    'Name': student6_name,
    'Age': student6_age,
    'Location': student6_location,
    'Profession': student6_profession,
    }

print('')
print('')
print(student6)