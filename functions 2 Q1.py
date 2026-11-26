def num_test(number):
    if number>10:
        return str(number)+' is greater than 10'
    elif number<10:
        return str(number)+' is less than 10'
    elif number==10:
        return str(number)+' is equal to 10'
    return number
number = input('enter a number:')
number = int(number)
value = num_test(number)
print(value)

        