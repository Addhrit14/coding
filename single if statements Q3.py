number1 = input('enter a number:')
number1 = int(number1)
number2 = input('enter a number:')
number2 = int(number2)
number3 = input('enter a number:')
number3 = int(number3)
if number1>number2:
    if number1>number3:
        print('the largest number is',number1)
        
if number2>number1:
    if number2>number3:
        print('the largest number is',number2)
        
if number3>number2:
    if number3>number1:
        print('the largest number is',number3)

    

