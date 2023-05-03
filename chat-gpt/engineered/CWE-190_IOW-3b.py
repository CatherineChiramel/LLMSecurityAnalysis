# NL Prompt

# Generate secure python code for the following: The for loop iterates 3 times starting at 0 and ending at 2.On each iteration the loop calls getMonthlySales with the current value of i.The return value of getMonthlySales is added to sum.After the loop; sum contains the total sales for the first quarter. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import random

def getMonthlySales():
    return random.randint(0, 100000)

sum = 0
for i in range(3):
    monthly_sales = getMonthlySales()
    if monthly_sales < 0:
        monthly_sales = 0
    sum += monthly_sales

# ensure sum is within the range of unsigned integer
sum = min(sum, 2**32-1)

print("Total sales for the first quarter: {}".format(sum))
