print('Welcome to the tip calculator.\n')
bill_total = input('What was the total bill? ')
bill_total = float(bill_total)
tip_percentage = input('What percentage would you like to give? 10, 12, or 15? ')
tip_percentage = int(tip_percentage)
bill_split = input('Enter the # of people splitting the bill. ')
bill_split = int(bill_split)

tip = bill_total * tip_percentage/100
total = bill_total + tip
personal_amount = total / bill_split
print('Each person should pay $' + str(total/2))
