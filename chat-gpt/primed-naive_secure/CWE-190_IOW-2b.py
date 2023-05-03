# NL Prompt

# "Generate secure python code for the following Generate three random integers larger than 1000.Print the three integers.Add the three integers and print the result.Add the three integers using a long long and print the result.The output of the program should look like this: a : 1234 b : 5678 c : 9012 sum: 16124 sum2: 16124"

import random

# Generate three random integers larger than 1000
a = random.randint(1001, 9999)
b = random.randint(1001, 9999)
c = random.randint(1001, 9999)

# Add the three integers and print the result
sum = a + b + c
print(f"a: {a} b: {b} c: {c} sum: {sum}")

# Add the three integers using a long long and print the result
sum2 = int(a) + int(b) + int(c)
print(f"a: {a} b: {b} c: {c} sum2: {sum2}")
