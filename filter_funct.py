#Even odd no's using filter Note: It only filter out the elements which are true
def check_num(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
l = [100,105,110,115,120,123,126]
result = list(filter(check_num,l))
print(result)
