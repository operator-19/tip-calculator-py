print('Welcom to tip Calculator!')
bill = float(input("What was the total bill? "))
tip = float(input(
    "How much tip would you like to give? 10, 12, or 15? ")) / 100 * bill + bill
# print(tip)
split = float(input('How many to split the bill? '))

sum = round(tip / split, 2)
print(f'Each person should pay: ${sum}')
