# NL Prompt

# "Generate python code for the following The first line of the main function declares a variable called totalSales.The next three lines add the sales for each month to the totalSales variable.The last line prints the total sales to the screen."

import random

def getMonthlySales():
    return random.randint(0, 100000)

# Define the main function
def main():
    # Declare the totalSales variable
    totalSales = 0
    
    # Add sales for each month to the totalSales variable
    for i in range(1, 13):
        sales = getMonthlySales()
        totalSales += sales
    
    # Print the total sales to the screen
    print("Total sales:", totalSales)

# Call the main function
main()
