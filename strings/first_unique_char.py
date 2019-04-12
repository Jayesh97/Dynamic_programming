from collections import OrderedDict
s = "GeeksforGeeks"

#dict 2 pass
d = {}
for i in s:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
for i in s:
    if d[i]==1:
        print(i)
        break

#using ordered dict
a = {}
for i,j in enumerate(s):
    if j in a:
        a[j][1] = a[j][1]+1
    else:
        a[j] = [0,0] #represents [location,count]
        a[j][0] = i
        a[j][1] = 1
print(a)
for k,v in a.items():
    if v[1]==1:
        print(k)
        break


        

