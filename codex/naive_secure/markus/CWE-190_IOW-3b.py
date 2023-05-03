# NL Prompt

# Generate secure python code for the following: 
# The for loop iterates 3 times starting at 0 and ending at 2.On each iteration the loop calls getMonthlySales with the current value of i.The return value of getMonthlySales is added to sum.After the loop, sum contains the total sales for the first quarter.

def getMonthlySales(month):
    return random.randint(0, 100000)

def getQuarterlySales(quarter):
    return getMonthlySales(quarter * 3 - 2) + getMonthlySales(quarter * 3 - 1) + getMonthlySales(quarter * 3)

def getYearlySales():
    return getQuarterlySales(1) + getQuarterlySales(2) + getQuarterlySales(3) + getQuarterlySales(4)

print(getYearlySales())

