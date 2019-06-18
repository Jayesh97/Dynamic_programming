a = [1,0,0,0,1,0,0]
n = 2
def flower(a,n):
    count = 0
    for i in range(len(a)):
        if a[i]==0 and (i==0 or a[i-1]==0) and (i==len(a)-1 or a[i+1]==0):
            a[i]=1
            count = count+1
        print(a)
        if count>=n:
            return True
    return False
print(flower(a,n))

