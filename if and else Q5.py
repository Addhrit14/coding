number1 = input('enter a number:')
number1 = int(number1)
negative = number1*-1
if number1 >= 0:
    print('the absolute value of',number1,'is',number1)
else:
    print('the absolute value of',number1,'is',negative)