rain = input('is it raining:')
if rain == 'yes':
    wind = input('is it windy:')
    if wind == 'no':
        print('take an umbrella')
    else:
        print('it is too windy for an umbrella')
else:
    print ('enjoy your day')
