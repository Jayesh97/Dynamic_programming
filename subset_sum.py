''''
2-D array with values filling per row basis
x - list of values
y - Total sum
'''
def matrix(k,l,val):
    k = [[0 for i in range(val+1)] for j in range(l+1)]
    for x in range(l+1):
        for y in range(val+1):
            if y==0:
                k[x][y]=1 #Represents True
            elif x==0:
                k[x][y]=0 #Represents False
            elif y>=a[x-1]: 
                delta = y - a[x-1]
                k[x][y] = k[x-1][delta] or k[x-1][y]
            else:
                k[x][y] = k[x-1][y]
    return k

def subset(s,x,y,item):
    if s[x][y] == 0:
        print("string cannot be formed")
    elif s[x][y] == s[x-1][y]:
        return subset(s,x-1,y,item)
    else:
        item.append(a[x-1]) #index of s is ahead of a
        y =  y - a[x-1]
        x = x-1
        if y==0:
            return item
        return subset(s,x,y,item)
        

val = 11
a = [2,3,7,8,10]
l = len(a)
s = matrix(a,l,val)
v = subset(s,l,val,[])
#print(s)
print(v)