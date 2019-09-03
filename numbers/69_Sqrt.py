x = 10
def sqrt(x):
    if x<2:
        return x
    left,right=2,x//2
    while left<right:
        pivot = (left+right)//2
        num=pivot*pivot
        if num==x:
            return pivot
        elif num>x:
            right=pivot-1
        else:
            left=pivot+1
    return right

print(sqrt(x))