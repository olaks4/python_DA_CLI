

English = input('Enter English Score: ')
Mathematics = input('Enter Mathematics Score: ')
print(type(English))

if English.isnumeric() and Mathematics.isnumeric():
    English = int(English)
    Mathematics = int(Mathematics)

    if ( English < 0 or English > 100 ) or ( 0 > Mathematics > 100 ):
        print('Student score should be between 0 and 100')
    else:
        if English > 49 and Mathematics > 49:
            print('Student eligible for UI and OAU admission')
        elif English > 49 or Mathematics > 49:
            print('Student is eligible for OAU admission')
        else:
            print('Omo, try again next year')
                    
else:
    print('You have entered invalid value for student scores')   
        
        
        
# try:
#     English_Score = int(English)
#     print(English_Score > 10)
# except:
#     print('Code not working')
    
# if English.isnumeric():
#     print('English score contains numbers only')
#     English_Score = int(English)
#     print(English_Score > 10)

# else:
#     print('English score does not contain numbers only')

'''
Collect a student score and return the corresponding grade
A1 = 75 - 100
B2 = 70 - 74
B3 = 65 - 69
C4 = 60 - 64
C5 = 55 - 59
C6 = 50 - 54
D7 = 45 - 49
E8 = 40 - 44
F9 = 0 - 39
# Example or eg: PRINT student grade is B3 for score of 67

FIZZBUZZ app
from a list of numbers
for each number
if the number is divisible by 3, print fizz.
if the number is divisible by 5, print buzz.
if the number is divisible by 3 and 5, print fizzbuzz.
if not print the number

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)




score_input = input('Enter score: ')
score = int(score_input)
if 75 <= score <= 100:
    print("student garde is A1 for score 75 <= score <= 100")
elif 70 <= score <= 74:
    print("student grade is B2 for score 70 <= score <= 74")
elif 65 <= score <= 69:
    print("student grade is B3 for score 65 <= score <= 69")
elif 60 <= score <= 64:
    print("student grade is c4 for score 60 <= score <= 64") 
elif 55 <= score <= 59:
    print("student grade is c5 for score 55 <= score <= 59")  
elif 50 <= score <= 54:
    print("student grade is c6 for score 50 <= score <= 54")
elif 45 <= score <= 49:
    print("student grade is D7 for score 45 <= score <= 49") 
elif 40 <= score <= 44:
    print("student grade is E8 for score40 <= score <= 44")  
elif 0 <= score <= 39:
    print("student grade is F9 for score 0 <= score <= 39")  
else:
    print("Invalid score")
