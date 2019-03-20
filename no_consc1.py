'''
same as fibonacci series total(n) --> total(n-1) + total(n-2) "last half is ruled out"
Menmonization applied
'''
def total(n):
    if n==2:
        return 3
    if n==1:
        return 2
    else:
        if a[n] != None:
            return a[n]
        else:   
            a[n] =  total(n-1) + total(n-2)
    return a[n]
n=5
a = [None,2,3]+[None]*(n-2)
t = total(n)
print(t)