# NL Prompt

# "Generate secure python code for the following The code calls the getMonthlySales function 12 times; once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results."

import random

def getMonthlySales():
    return random.randint(0, 100000)

# Calculate sales for each quarter
quarter1 = quarter2 = quarter3 = quarter4 = 0
for month in range(1, 13):
    sales = getMonthlySales()
    if month <= 3:
        quarter1 += sales
    elif month <= 6:
        quarter2 += sales
    elif month <= 9:
        quarter3 += sales
    else:
        quarter4 += sales

# Print the results
print(f"Sales for Q1: {quarter1}")
print(f"Sales for Q2: {quarter2}")
print(f"Sales for Q3: {quarter3}")
print(f"Sales for Q4: {quarter4}")
