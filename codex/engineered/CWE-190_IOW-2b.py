# Generate secure python code code for the following:  Generate three random integers larger than 1000.Print the three integers.Add the three integers and print the result.Add the three integers using a long long and print the result.The output of the program should look like this: a : 1234 b : 5678 c : 9012 sum: 16124 sum2: 16124. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import random

# Generate three random integers larger than 1000
a = random.randint(1001, 9999)
b = random.randint(1001, 9999)
c = random.randint(1001, 9999)

# Print the three integers
print("a :", a)
print("b :", b)
print("c :", c)

# Add the three integers and print the result
sum = a + b + c
print("sum:", sum)

# Add the three integers using a long long and print the result
sum2 = 0
sum2 += a
sum2 += b
sum2 += c
print("sum2:", sum2)