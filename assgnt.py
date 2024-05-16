               number_list = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

def fizzbuzz(number_list):
    for number in number_list:
        if number % 3 == 0 and number % 5 == 0:
            print('fizzbuzz')
        elif number % 3 == 0:
            print('fizz')
        elif number % 5 == 0:
            print('buzz')
        else:
            print(number)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

fizzbuzz(number_list)







""""
1. write a program to count the number of even and odd numbers in a range of numbers
 e.g: print ('Number of Odd numbers in the list is 12')
2. write a program to convert temperature to celsius from fahrenheit and vice versa
"""


list_of_even_numbers = []
list_0f_Odd_numbers = []

range_number = input('Enter the range')

try:
    range_number = int(range_number)

    for i in range(1, range_number):
        if i % 2 != 0:
            #print(f'{i} - Odd number')
            list_0f_Odd_numbers.append(i)
        else:
            #print(f'{i} - Even number')
            list_of_even_numbers.append(i)

    # print('Even list - ', list_of_even_numbers)
    # print('Even list - ', list_of_Odd_numbers)
    total_even = len(list_of_even_numbers)
    total_Odd = len(list_0f_Odd_numbers)
    print('')
    print(f'The total number of even in the list - {total_even}')
    print(f'The total number of Odd in the list - {total_Odd}')
except:
    print('The range you entered is invalid, please enter a number')

    