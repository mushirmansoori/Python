import re
s = "+91 7123456789"
r = re.compile("(?:\+91\s)?([6-9][0-9]{9})")
m = re.search(r,s)
if m:
    print(m.group(1))
else:
    print("Contact Number not found")
