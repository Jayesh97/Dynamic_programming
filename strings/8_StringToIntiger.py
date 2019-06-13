import re

st = "42withwords"
total = 0
matched = re.match(r'^ *([\+-]?\d+){1}',st)
print(int(matched.group()))
string = matched.group()
for i in string:
    total = total*10+ord(i)-ord('0')
print(total)