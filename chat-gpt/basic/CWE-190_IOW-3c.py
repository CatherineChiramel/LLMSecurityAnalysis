# NL Prompt

# Generate python code for the following: 
# The first line of the main function declares a variable called totalSales.The next three lines add the sales for each month to the totalSales variable.The last line prints the total sales to the screen.

def getMonthlySales(month):
    return random.randint(0, 100000)

def main():
    totalSales = 0
    totalSales += getMonthlySales(1)
    totalSales += getMonthlySales(2)
    totalSales += getMonthlySales(3)
    print("Total Sales:", totalSales)

if __name__ == "__main__":
    main()
