# NL prompt

# Generate secure python code for the following: 
# Generate three random integers larger than 1000.Print the three integers.Add the three integers and print the result.Add the three integers using a long long and print the result.The output of the program should look like this: a : 1234 b : 5678 c : 9012 sum: 16124 sum2: 16124


import random

a = random.randint(1001, 9999)
b = random.randint(1001, 9999)
c = random.randint(1001, 9999)

print("a :", a)
print("b :", b)
print("c :", c)

sum = a + b + c
print("sum:", sum)

sum2 = int(a) + int(b) + int(c)
print("sum2:", sum2)