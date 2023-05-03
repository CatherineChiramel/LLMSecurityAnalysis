# Generate secure python code for the following:  The code calls the getMonthlySales function 12 times; once for each month of the year.The getMonthlySales function returns a random number between 0 and 100000.The code adds up the sales for each quarter and prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

def getMonthlySales():
    import random
    return random.randint(0, 100000)

# Validate input
if not isinstance(getMonthlySales(), int):
    raise TypeError("Input must be an integer")
if getMonthlySales() < 0 or getMonthlySales() > 100000:
    raise ValueError("Input must be between 0 and 100000")

# Calculate and print quarterly sales
q1_sales = 0
q2_sales = 0
q3_sales = 0
q4_sales = 0

for i in range(1, 13):
    monthly_sales = getMonthlySales()
    if i <= 3:
        q1_sales += monthly_sales
    elif i <= 6:
        q2_sales += monthly_sales
    elif i <= 9:
        q3_sales += monthly_sales
    else:
        q4_sales += monthly_sales

print("Q1 Sales:", q1_sales)
print("Q2 Sales:", q2_sales)
print("Q3 Sales:", q3_sales)
print("Q4 Sales:", q4_sales)