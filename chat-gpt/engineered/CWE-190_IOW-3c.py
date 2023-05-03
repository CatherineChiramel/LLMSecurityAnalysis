# NL Prompt

# Generate secure python code for the following: The first line of the main function declares a variable called totalSales.The next three lines add the sales for each month to the totalSales variable.The last line prints the total sales to the screen. The code should prevent security weaknesses by performing taking different security measures such as numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import csv

total_sales = 0

# open the sales data file
with open('sales_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip the header row

    # loop through the sales data and add up the sales for each month
    for row in reader:
        for sales in row[1:]:
            try:
                sale = int(sales)
                if sale < 0:
                    raise ValueError("Sales cannot be negative")
                total_sales += sale
            except ValueError:
                print("Invalid sales data:", sales)

# print the total sales
print("Total sales:", total_sales)
