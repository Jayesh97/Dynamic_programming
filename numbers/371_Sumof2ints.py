a = 5 #101
b = 2 #010

def getsum(a,b):
        while b!=0:
            c=a&b
            print(c)
            a=a^b
            b=c<<1
        return a
        
print(getsum(a,b))