x = 255
n = -3
def power(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n in power.d:
        return power.d[n]
    n1 = int(n/2)
    n2 = n-n1
    power.d[n1]=power(x,n1)
    power.d[n2]=power(x,n2) 
    return power.d[n1]*power.d[n2]
power.d = {}
if n<0:
    print(float(1)/power(x,abs(n)))
else:
    print(power(x,n))