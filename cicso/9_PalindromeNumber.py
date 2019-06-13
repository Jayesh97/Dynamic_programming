x = 121
def palin(x):
    if x<0 or x%10==0:
        return False  
    rev = 0 
    y = x
    while x>0:
        rem = x%10
        rev = rev*10 + rem
        x = x/10
    #print(rev)
    if rev==y: return True
    return False
print(palin(x))
