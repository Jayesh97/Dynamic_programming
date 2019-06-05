'''
This is longest common substring
This is different from longest common subsequence
'''
s = [0,0,0,0,1]
t = [1,0,0,0,0]
k = [[0 for x in range(len(s))] for y in range(len(t))]
#print(k)
#traversing horizontal
maxx = 0
for i in range(len(t)):
    for j in range(len(s)):
        if(s[j]==t[i]):
            if i==0 or j==0:
                k[i][j] = 1
            else:
                k[i][j] = k[i-1][j-1]+1
            if k[i][j] > maxx:
                maxx = k[i][j]
        else:
            k[i][j] = 0
print(k)
print(maxx)

