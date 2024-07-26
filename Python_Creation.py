correct_year = 1994
while True:
    User_input = int(input('When was Python 1.0 released? '))
    if User_input > correct_year:
        print('It was earlier than that!')
    elif User_input < correct_year:
        print('It was later than that!')
    else:
        print('correct! ')
        break


#while True: creates an infinite loop that will run indefinitely until explicitly broken by a break statement or another condition that stops the loop.
#It is commonly used when you need to repeatedly execute a block of code but the exact number of iterations is not known ahead of time.