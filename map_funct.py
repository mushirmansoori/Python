#squarring values in list using map
def sqr(num1):
    return num1**2
l = [10,20,30,40,50,60,70]

#typecast it in a list
result = list(map (sqr,l))
print(result)
for value in result:
    print(value)
    
    
#adding two no's of two lists using map    
def add(num1,num2):
    return num1 + num2 
l = [100,200,300,400,500]
l1 = [10,20,30,40,50]
result = list(map(add,l,l1))
print(result)
