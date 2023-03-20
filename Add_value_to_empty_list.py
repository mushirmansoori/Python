def add_value(*k):
    l = []
    for value in k:
        l.append(value)
    return l
result = add_value(100,200,300,400,500)
print(result)
result = add_value(600,700,800,900)
print(result)
