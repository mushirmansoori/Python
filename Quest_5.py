# Factorial of any no n is represented by n! and is equal to 1*2*3*....*(n-1)*n
#Eg.  
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also 
# 1! = 1
# 0! = 1
# Write a prog to calculate factorial of a number
# Define the number for which you want to calculate the factorial
n = 5

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a loop
for i in range(1, n+1):
    factorial *= i

# Print the factorial
print(f"The factorial of is ", n, factorial)
