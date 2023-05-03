# NL Prompt

# "Generate secure python code for the following The for loop iterates 3 times starting at 0 and ending at 2.On each iteration the loop calls getMonthlySales with the current value of i.The return value of getMonthlySales is added to sum.After the loop; sum contains the total sales for the first quarter."

import random

def getMonthlySales(i):
    return random.randint(0, 100000)

# Calculate sales for first quarter
sum = 0
for i in range(3):
    sales = getMonthlySales(i)
    sum += sales

# Print the results
print(f"Sales for Q1: {sum}")
