def display(row1, row2, row3):
    print(f'{row1}\n{row2}\n{row3}')

row1 =[' ', ' ', ' ']
row2 =[' ', ' ', ' ']
row3 =[' ', ' ', ' ']
display(row1, row2, row3)

def user_choice():
    
    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_range = false


    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter a number (0-10): ')

        if choice.isdigit() == False:
            print('Sorry that is not a digit')

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are out of acceptable range (0-10)')
                within_range == False

    return int(choice)

