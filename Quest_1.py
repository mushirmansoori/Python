#python code to find those numbers which are divisible by 7 and 5, between 1500 and 2700 (both included)

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
        
        #OR another way using whiile loop
a = 1500
b = 2700
while a <= b:
    if a % 5 == 0 and a % 7 == 0:
        print(a)
    a += 1
