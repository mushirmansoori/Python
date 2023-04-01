import re
s = "01-04-2023"
r = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
m = re.search(r,s)
if m:
    print(m.group("year"))
else:
    print("Pattern not found")
