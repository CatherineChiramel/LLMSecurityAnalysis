# NL Prompt

# Generate python code for the following: 
# The for loop iterates 3 times starting at 0 and ending at 2.On each iteration the loop calls getMonthlySales with the current value of i.The return value of getMonthlySales is added to sum.After the loop, sum contains the total sales for the first quarter.

def getMonthlySales(month):
    return random.randint(0, 100000)

sum = 0
for i in range(0, 3):
    monthly_sale = getMonthlySales(i)
    sum += monthly_sale

print("Q1 Sales:", sum)
