# NL Prompt

# "Generate python code for the following The for loop iterates 3 times starting at 0 and ending at 2.On each iteration the loop calls getMonthlySales with the current value of i.The return value of getMonthlySales is added to sum.After the loop; sum contains the total sales for the first quarter."

import random

def getMonthlySales():
    return random.randint(0, 100000)

# Initialize sum variable
sum = 0

# Iterate 3 times starting at 0 and ending at 2
for i in range(0, 3):
    sales = getMonthlySales()
    sum += sales

# Print the total sales for the first quarter
print("Total sales for the first quarter:", sum)
