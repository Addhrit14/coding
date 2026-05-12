score = input('enter your score:')
score = int(score)
if  90 <= score <= 100:
    print('your grade is A')
    if  80 <= score <= 89:
        print('your grade is B')
        if  70 <= score <= 79:
            print('your grade is C')
            if  60 <= score <= 69:
                print('your grade is D')
                if  0 <= score <= 59:
                    print('your grade is F')
else:
    print('invalid')
    