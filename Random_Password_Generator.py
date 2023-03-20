import random
def gen_password(Length=8):
    l = ['@','&','#','$']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    password = upper + lower + special + str(digit)
    l=random.sample(password,Length)
    password = ("").join(l)
    return password
result = gen_password()
print(result)
