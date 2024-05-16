'''
Create a list of at least 5 states and capital.
From user option 1-4
1. Read - display all stats and capital
2. Create - User can add a state and it capital
3. Update - User can edit a particular state and capital
4. Delete - User can delete a particular state and capital




CG

Create a list of at least 5 states and capital.
From user option 1-4
1. Read - display all stats and capital
2. Create - User can add a state and it capital
3. Update - User can edit a particular state and capital
4. Delete - User can delete a particular state and capital
write a python function that performs each option based on user input


state1 = { 'State': 'Oyo', 'Capital': 'Ibadan'}
state2 = { 'State': 'Lagos', 'Capital': 'Ikeja'}
state3 = { 'State': 'Ogun', 'Capital': 'Abeokuta'}
state4 = { 'State': 'Osun', 'Capital': 'Osogbo'}
state5 = { 'State': 'Ekiti', 'Capital': 'Ado-Ekiti'}

stateCapital_list = [state1, state2, state3, state4, state5]
'''

'''

state1 = { 'State': 'Oyo', 'Capital': 'Ibadan'}
state2 = { 'State': 'Lagos', 'Capital': 'Ikeja'}
state3 = { 'State': 'Ogun', 'Capital': 'Abeokuta'}
state4 = { 'State': 'Osun', 'Capital': 'Osogbo'}
state5 = { 'State': 'Ekiti', 'Capital': 'Ado-Ekiti'}

stateCapital_list = [state1, state2, state3, state4, state5]

def stateCapital():
    print("""
    Enter 1 to view list of states and capital
    Enter 2 to add a state and capital
    Enter 3 to edit a state of you choice
    Enter 4 to delete a particular state and it capital
    Enter 5 to close the program
    """)
    
    user_input = input('Enter your option: ')

    stateList = []
    for state_capital in stateCapital_list:
        state = f'{state_capital["State"]} : {state_capital["Capital"]}'
        stateList.append(state)

    stateList.sort()

    def read():
        
        num = 1
        for eachState in stateCapital_list:
            print(f'{num}. {eachState}')
            num += 1

    if user_input == '1':
        print('View list of states and capital\n')
        read()

        stateCapital()


    elif user_input == '2':
        print('Add a state and capital\n')
        getState = input('Enter state: ')
        getCapital = input('Enter capital: ')
        state_capital = {
                'State' : getState,
                'Capital' : getCapital
            }
        
        stateCapital_list.append(state_capital)

        read()

        stateCapital()

    elif user_input == '3':
        print('Edit a state of you choice\n')
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1
        # read()
        index = input('\nEnter the number of the state: ')
        
        indexInt = int(index)
        print(stateCapital_list[indexInt-1])

        stateCapital_list[indexInt-1]['State'] = input('Enter new state')
        stateCapital_list[indexInt-1]['Capital'] = input('Enter new capital')
        
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1

        # try:
        # except:
        #     print('Error with your input')

        stateCapital()

    elif user_input == '4':
        print('Delete a particular state and it capital')
        
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1
        # read()
        index = input('\nEnter the number of the state to delete: ')
        indexInt = int(index)
        print(stateCapital_list[indexInt-1])
        item = stateCapital_list[indexInt-1]
        stateCapital_list.remove(item)
        
        
        num = 1
        for state_capital in stateCapital_list:
            state = f'{state_capital["State"]} : {state_capital["Capital"]}'
            print(f'{num}. {state}')
            num += 1

        stateCapital()

    elif user_input == '5':
        print('Thank you for using our software')

    else:
        print('Input invalid')
        stateCapital()
        
stateCapital()

'''


def display_states(states):
    print("States and Capitals:")
    for idx, state in enumerate(states, start=1):
        print(f"{idx}. {state['State']} - {state['Capital']}")

def add_state(states):
    state_name = input("Enter the name of the state: ")
    capital_name = input("Enter the capital of the state: ")
    new_state = {'State': state_name, 'Capital': capital_name}
    states.append(new_state)
    print("State and capital added successfully!")

def edit_state(states):
    display_states(states)
    index = int(input("Enter the index of the state to edit: ")) - 1
    if 0 <= index < len(states):
        new_state_name = input("Enter the new name of the state: ")
        new_capital_name = input("Enter the new capital of the state: ")
        states[index]['State'] = new_state_name
        states[index]['Capital'] = new_capital_name
        print("State and capital updated successfully!")
    else:
        print("Invalid index!")

def delete_state(states):
    display_states(states)
    index = int(input("Enter the index of the state to delete: ")) - 1
    if 0 <= index < len(states):
        del states[index]
        print("State and capital deleted successfully!")
    else:
        print("Invalid index!")

def main():
    state1 = { 'State': 'Oyo', 'Capital': 'Ibadan'}
    state2 = { 'State': 'Lagos', 'Capital': 'Ikeja'}
    state3 = { 'State': 'Ogun', 'Capital': 'Abeokuta'}
    state4 = { 'State': 'Osun', 'Capital': 'Osogbo'}
    state5 = { 'State': 'Ekiti', 'Capital': 'Ado-Ekiti'}

    stateCapital_list = [state1, state2, state3, state4, state5]

    while True:
        print("\nOptions:")
        print("1. Read")
        print("2. Create")
        print("3. Update")
        print("4. Delete")
        print("5. Quit")
        
        option = input("Enter your choice (1-5): ")
        
        if option == '1':
            display_states(stateCapital_list)
        elif option == '2':
            add_state(stateCapital_list)
        elif option == '3':
            edit_state(stateCapital_list)
        elif option == '4':
            delete_state(stateCapital_list)
        elif option == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please choose between 1 to 5.")

# if __name__ == "__main__":
#     main()
main()



'''
data1 = {
    'Name': "ADAMS",
    'ID': 'E7876',
    'SALARY': 50000,
    'DEPARTMENT': 'ACCOUNTING'
}
data2 = {
    'Name': "JONES",
    'ID': 'E7499',
    'SALARY': 45000,
    'DEPARTMENT': 'RESEARCH'
}
data3 = {
    'Name': "MARTIN",
    'ID': 'E7900',
    'SALARY': 50000,
    'DEPARTMENT': 'SALES'
}
data4 = {
    'Name': "SMITH",
    'ID': 'E7698',
    'SALARY': 55000,
    'DEPARTMENT': 'OPERATIONS'
}

Task1: 
Use "assign_department" method to change the department of an employee

Task2: to calculate overtime salary
Use "calculate_emp_salary" method takes two arguments: salary and hours_worked,
which is th number of hour worked by th employee.
If the number of hours worked is more than 50, the method computes overtime
and adds it to the salary.
Overtime is calculated using the following formula:

overtime = hours_worked - 50
overtime_amount = overtime * (salary/50)



'''
