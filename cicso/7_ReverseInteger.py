x = -123
def reverse(x):
    rev = 0
    if x>0:
        while x>0:
            rem = x%10
            rev = rev*10+rem
            x = x/10
        return rev
    if x<0:
        x = -x
        return -reverse(x)
print(reverse(x))