# Generate secure python code for the following:  The for loop iterates 3 times starting at 0 and ending at 2.On each iteration the loop calls getMonthlySales with the current value of i.The return value of getMonthlySales is added to sum.After the loop; sum contains the total sales for the first quarter. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

sum = 0
for i in range(0, 3):
    # Validate input
    if not isinstance(i, int) or i < 0 or i > 2:
        raise ValueError('i must be an unsigned integer between 0 and 2')
    # Call getMonthlySales
    monthly_sales = getMonthlySales(i)
    # Validate return value
    if not isinstance(monthly_sales, int) or monthly_sales < 0:
        raise ValueError('monthly_sales must be an unsigned integer')
    # Add to sum
    sum += monthly_sales

# sum contains the total sales for the first quarter
print(sum)