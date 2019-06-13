s = "abcd"
t = "abcde"
s = sorted(s)
t = sorted(t)
for i,j in enumerate(s):
    if j != t[i]:
        print(t[i])
print(t[len(s)])