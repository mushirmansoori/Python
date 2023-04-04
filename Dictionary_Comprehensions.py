#printing the square of values in dictionary, using dictionary comprehension
d = {x:x**2 for x in range(1,11)}
print(d)

#printing asscii values using dictionary comprehension
d = {chr(x):x for x in range(97,123)}
print(d)

#swapping ASCII values using dictionary comprehension
d = {chr(x):x for x in range(97,123)}
d2 = {value:key for key, value in d.items()}
print(d2)
