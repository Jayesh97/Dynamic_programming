str1 = "characters"
str2 = "alphabets"
d = {}
for i in str1:
    d[i]=0
for i in str2:
    if i in d:
        d[i]=1
    else:
        d[i]=0
#values with 1 - common chars
#values with 0 - uncommon chars
l = []
for k,v in d.items():
    if v==0:
        l.append(k)
print(l)