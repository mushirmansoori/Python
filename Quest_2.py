#a python prog to count the no of even and odd numbers from a series of numbers 
#Sample nos 
#nos= (1,2,3,4,5,6,7,8,9)
#Expected output 
#No of even nos : 4
#No of odd nos: 5

Num = (1,2,3,4,5,6,7,8,9)
even_count=0
odd_count=0
for Nos in Num:
    if Nos % 2 == 0:
        even_count +=1
    else:
        odd_count +=1
print("No of even nos", even_count)
print("No of odd nos",  odd_count)
