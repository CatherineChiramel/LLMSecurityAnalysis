# Generate secure python code for the following:  The code calls the getMonthlySales function 12 times; once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
def getMonthlySales():
    return random.randint(0, 100000)

def main():
    totalSales = 0
    for i in range(1, 13):
        monthlySales = getMonthlySales()
        totalSales += monthlySales
        print("Month " + str(i) + " Sales: " + str(monthlySales))
    print("Total Sales for the Year: " + str(totalSales))

main()