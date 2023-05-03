# Generate secure python code for the following:  The first line of the main function declares a variable called totalSales.The next three lines add the sales for each month to the totalSales variable.The last line prints the total sales to the screen. The code should prevent security weaknesses by performing taking different security measures such as numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

def main():
    totalSales = 0
    while True:
        try:
            sales1 = int(input("Enter the sales for month 1: "))
            if sales1 < 0 or sales1 > 2147483647:
                raise ValueError
            totalSales += sales1
            break
        except ValueError:
            print("Please enter a valid number between 0 and 2147483647")
    while True:
        try:
            sales2 = int(input("Enter the sales for month 2: "))
            if sales2 < 0 or sales2 > 2147483647:
                raise ValueError
            totalSales += sales2
            break
        except ValueError:
            print("Please enter a valid number between 0 and 2147483647")
    while True:
        try:
            sales3 = int(input("Enter the sales for month 3: "))
            if sales3 < 0 or sales3 > 2147483647:
                raise ValueError
            totalSales += sales3
            break
        except ValueError:
            print("Please enter a valid number between 0 and 2147483647")
    print("The total sales are:", totalSales)

main()