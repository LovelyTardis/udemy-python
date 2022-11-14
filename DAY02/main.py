'''
    This project is based on a company that all employees takes a 13% commission for all sells every month.
    The program will ask the name and total amount of sells that the employee has done.
    Prints a sentence that will give the name and the commission.
'''
# constant variable
COMMISSION_PERCENTAGE = 13

name = input("Employee name: ")
amount_sells = float(input("This month sells amount: "))
total_commission = round(amount_sells * (COMMISSION_PERCENTAGE / 100), 2)

print(f"Hi, {name}!\nYour commission this month is {total_commission}€, {COMMISSION_PERCENTAGE}% of your sells!")
