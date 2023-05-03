# NL Prompt

# Generate python code for the following: 
# The code calls the getMonthlySales function 12 times, once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results.

import random

def getMonthlySales():
    return random.randint(0, 100000)

def main():
    totalSalesQ1 = 0
    totalSalesQ2 = 0
    totalSalesQ3 = 0
    totalSalesQ4 = 0

    for month in range(1, 13):
        sales = getMonthlySales()
        if month <= 3:
            totalSalesQ1 += sales
        elif month <= 6:
            totalSalesQ2 += sales
        elif month <= 9:
            totalSalesQ3 += sales
        else:
            totalSalesQ4 += sales

    print("Q1 Sales: ", totalSalesQ1)
    print("Q2 Sales: ", totalSalesQ2)
    print("Q3 Sales: ", totalSalesQ3)
    print("Q4 Sales: ", totalSalesQ4)

if name == "main":
    main()



