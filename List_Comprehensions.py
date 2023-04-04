#for printing the square of each value in the list, using list comprehension 
l = [100,200,300,400,500,600]
l2 = [value*value for value in l]
print(l2)

#for printing even no's using list comprehension
l = [10,20,25,30,35,40,50,55]
l2 = [value for value in l if value%2 == 0]
print(l2)

#for getting the length of the value from list, using list comprehension
l = ['abc','abcd','abcde','bhvhvghgghchgc','abcdef']
l2 = [len(value) for  value in l]
print(l2)

#nested loop using list comprehension
l2 = [(value,value2) for value in range (1,5) for value2 in range (100,103)]
print(l2)

#for converting into a single list from a list within a list
l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = []
for value in l:
    for val2 in value:
        l2.append(val2)
print(l2)

#for converting into a single list from a list within a list using list comprehension
l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [val2 for value in l for val2 in value]
print(l2)

#finding even odd no's from list using list comprehension 
l = [10,13,15,20,24,27,30]
l2 = ["Even No" if value%2 == 0 else "Odd No" for value in l]
print(l,l2)
