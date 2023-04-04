#squaring values in list using lamda functions
l = [10,20,30,40,50,60,70]

#typecast it in a list
result = list(map(lambda num1:num1**2 ,l))
print(result)


#Even odd no's using filter and lambda
l = [100,105,110,115,120,123,126]
result = list(filter(lambda num:num % 2 == 0,l))
print(result)


#sorting a dictionary on a basis of values using lambda
d ={1:50,2:40,3:30,4:20,5:10}
l = sorted(d.items(),key=lambda x:x[1])
print(l)
