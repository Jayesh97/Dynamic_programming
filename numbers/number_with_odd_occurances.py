a = [1, 2, 3, 2, 3, 1, 3]
d = {}

#using dict with count as values
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

for k,v in d.items():
    if v%2 != 0:
        print(k)

#using xor
value = 0 
for i in a:
    value = value ^ i
print(value)