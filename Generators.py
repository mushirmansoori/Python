l = [10,20,30,40,50,60]
def printVal(l):
    for value in l:
        print(value)
printVal(l)


#fibonacci series using generator function Note: Generator will maintain the state and it gives one value at a time.

def fibo():
    first_num = 0
    second_num = 1
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num,second_num = second_num,next_val
g = fibo()
for value in range(10):
    print(next(g))
for value in range(20):
    print(next(g))
    
 
#Note: suppose you are getting large series of number you can convert to a generator expression and then using the next function you can fetch the value.
#square of each number using list comprehension.

l = [10,20,30,40,50,60]
l2 = (value*value for value in l)
print(next(l2))
print(next(l2))
