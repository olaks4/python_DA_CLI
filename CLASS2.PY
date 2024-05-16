#Integers: TYPES- Float, Complex & Boolean
num1 = 64
num2 = 304

#Operators
#Python divides the operators in the following groups:

# 01. Arithmetic operators

print(num1 + num2) #addition
print(num1 - num2) #Subtraction
print(num1 / num2) #Division
print(num1 * num2) #Multiplication
print(num1 % num2) #Modulus (returns the remainder)
print(num1 ** num2) #Exponential: num1 raise to power num2
print(num1 // num2) #Floor division

n1 = 5
n2 = 2
print('Divide 5 by 2')
print(n1 / n2) 
print(n1 % n2)

print('Exponential')
n1 = 5
n2 = 3
print(n1 ** n2)

print('Floor division')
print(type('Floor division'))
n1 = 127
n2 = 17
result1 = n1 / n2
print(result1)
print(type(result1))

result2 = n1 // n2
print(result2)
print(type(result2))

print('complex')
comp = 12e5
print(comp)
print(type(comp))


#Boolean
#We use boolean for comparison
#comparison operator
tr = True
fl = False

n1 = 8
n2 = 5
print(n1 > n2)
print(type(n1 > n2))

# Python Collection/Array
# LIST

Student_list = ['Ibrahim', 'Matthias', 'Bukola', 'Babatunde', 'Abeeb']
age_list = [21, 13, 46, 7]

print(Student_list)
print(len(Student_list))
print(Student_list[1])

second_student = Student_list[1]
print(second_student[4: ])
print(Student_list[1][4: ])

Student_list.append('Samuel') # Adding new item to the end of a list []
print(Student_list)
Student_list.pop() # Remove the last item from a list
print(Student_list)
Student_list.pop(2) # Removean item at a position in the list
print(Student_list)
Student_list.sort() # Arranges in a sequence
age_list.sort() # Arranges in sequence
print(Student_list)
print(age_list)
Student_list.reverse() # Arranges in reverse sequence 
print(Student_list)
