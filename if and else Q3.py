monthly_sales = input('enter your monthly sales:')
monthly_sales = int(monthly_sales)
commission1 = monthly_sales/100*15
commission2 = monthly_sales/100*5
if monthly_sales>40000:
    print('your commission for the month is',commission1)
else:
    print('your commission for the month is',commission2)
    
    
    