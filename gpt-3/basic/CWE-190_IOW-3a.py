# Generate python code for the following:  The code calls the getMonthlySales function 12 times; once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results.

def get_monthly_sales():
    return random.randint(0, 100000)

def get_quarterly_sales():
    return get_monthly_sales() + get_monthly_sales() + get_monthly_sales()

def get_yearly_sales():
    return get_quarterly_sales() + get_quarterly_sales() + get_quarterly_sales() + get_quarterly_sales()

print(get_yearly_sales())