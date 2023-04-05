#using iterators
l = [100,200,300,400,500]
i = iter(l)
for value in i:
    print(value)
    
#combing multiple lists usinting iterator
import itertools
l = [10,20,30,40,50]
l1 = [100,200,300,400,500]
l2 = [1000,2000,3000,4000,5000]
i = itertools.chain(l,l1,l2)
for value in i:
    print(value)
 
#list iteration multiple time's  Note: Cycle method will create infinite iterator over list 'l', so have to provide a condition to stop the execution.  
import itertools
l = [10,20,30,40,50]
count = 0
for value in itertools.cycle(l):
    if count < 20:
        print(value)
    else:
        break
    count+=1
 
 
#to get the same list in every iteration
import itertools
l = [10,20,30,40,50]
count = 0
for value in itertools.repeat(l):
    if count < 20:
        print(value)
    else:
        break
    count+=1

#iterate over the same list again
import itertools 
l = [10,20,30,40,50]
i = iter(l)
t = itertools.tee(i)
print(t)
for value in t[0]:
    print(value)
for value in t[1]:
    print(value)
 
 
#slicing in iterator
import itertools
l = [10,20,30,40,50]
l1 = [100,200,300,400,500]
l2 = [1000,2000,3000,4000,5000]
i = itertools.chain(l,l1,l2)
for value in itertools.islice(i,0,8):
    print(value)
 
 
#selecting two no's from the list using permutation method
l = [1,2,3,4]
print(list(itertools.permutations(l,2)))

#selecting two no's from the list using combinations method
print(list(itertools.combinations(l,2)))
