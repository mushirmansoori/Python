#Write a python prog to calculate the sum and avg of n interger nos.
# Define the sequence of integers
numbers = [5, 10, 15, 20, 25]

# Initialize sum and count variables to zero
sum = 0
count = 0

# Loop through the sequence of integers and add them to the sum variable
for num in numbers:
    sum += num
    count += 1

# Calculate the average by dividing the sum by the count
    avg = sum / count

# Print the sum and average
print("The sum of the integers is:", sum)
print("The average of the integers is:", avg)
