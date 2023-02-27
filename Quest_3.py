#Write a python prog which iterates the int from 1 to 50 for multiples of 3 print "fizz" instead of the no and for the multiple of 5 print "Buzz". For nos which are multiple of both print "FizzBuzz".
#Sample Output: 
#FizzBuzz
#1 
#2
#Fizz
#4
#Buzz
for num in range (1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
