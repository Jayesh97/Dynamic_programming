'Finding left half, right half and stitching it together'
def rotate(num,c):
    l = len(str(num))
    right = num//(10**(l-c)) 
    left = (num%(10**(l-c)))*(10**c)
    return left+right

c = 5
a = 12345
print(rotate(a,c))