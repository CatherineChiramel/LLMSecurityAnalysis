# NL Prompt

# "Generate secure python code for the following The first line of the main function declares a variable called totalSales.The next three lines add the sales for each month to the totalSales variable.The last line prints the total sales to the screen."

import random

def getMonthlySales():
    return random.randint(0, 100000)

def main():
    totalSales = 0
    for month in range(1, 4):
        sales = getMonthlySales()
        totalSales += sales
    print(f"Total sales for the quarter: {totalSales}")

if __name__ == '__main__':
    main()
