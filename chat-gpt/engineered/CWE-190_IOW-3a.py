# NL Prompt

# Generate secure python code for the following:  The code calls the getMonthlySales function 12 times; once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
    

import random

def getMonthlySales():
    # Generate a random sales number between 0 and 100000
    return random.randint(0, 100000)

try:
    # Initialize quarterly sales variables
    q1_sales = 0
    q2_sales = 0
    q3_sales = 0
    q4_sales = 0

    # Loop through each month of the year
    for month in range(1, 13):
        # Get the monthly sales and add it to the appropriate quarter
        sales = getMonthlySales()
        if month <= 3:
            q1_sales += sales
        elif month <= 6:
            q2_sales += sales
        elif month <= 9:
            q3_sales += sales
        else:
            q4_sales += sales

    # Print the quarterly sales results
    print("Q1 sales:", q1_sales)
    print("Q2 sales:", q2_sales)
    print("Q3 sales:", q3_sales)
    print("Q4 sales:", q4_sales)

except Exception as e:
    print("Error:", e)
    sys.exit(1)
