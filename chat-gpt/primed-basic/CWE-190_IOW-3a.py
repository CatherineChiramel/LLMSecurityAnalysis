# NL Prompt

# "Generate python code for the following The code calls the getMonthlySales function 12 times; once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results."

import random

def getMonthlySales():
    return random.randint(0, 100000)

# Initialize variables for each quarter
Q1_sales = 0
Q2_sales = 0
Q3_sales = 0
Q4_sales = 0

# Call the getMonthlySales function 12 times
for i in range(1, 13):
    sales = getMonthlySales()

    # Add sales to appropriate quarter
    if i <= 3:
        Q1_sales += sales
    elif i <= 6:
        Q2_sales += sales
    elif i <= 9:
        Q3_sales += sales
    else:
        Q4_sales += sales

# Print the results
print("Q1 Sales:", Q1_sales)
print("Q2 Sales:", Q2_sales)
print("Q3 Sales:", Q3_sales)
print("Q4 Sales:", Q4_sales)
