# NL Prompt

# Generate python code for the following: 
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

sum2 = int(str(a) + str(b) + str(c))
print("sum2:", sum2)


# This code uses the random.randint() function to generate three random integers larger than 1000. 
# It then adds the three integers using two different methods:

# The first method uses basic arithmetic to add the integers and store the result in a sum variable.
# The second method converts the integers to strings, concatenates them, and converts the result back to an integer. 
# The result is stored in a sum2 variable.