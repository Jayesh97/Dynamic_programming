num = 11
den = 4
def fraction(num,den):
    if not num:
        return "0"
    sign = 1 if (num<0 and den<0) or (num>0 and den>0) else -1
    num,den = abs(num),abs(den)
    left = str(num//den)
    num = num%den
    print(left,num)
    if num==0:
        return left if sign==1 else "-"+left
    d = {}
    right = []
    i = 0
    print(num)
    while num:
        if num in d:
            print(right)
            right.insert(d[num],'(')
            right.append(')')
            break
        else:
            d[num]=i
            num = num*10
            div = num//den
            right.append(str(div))
        num = num%den
        i=i+1
    print(right)
    return left+'.'+''.join(right) if sign==1 else '-'+left+'.'+''.join(right)

print(fraction(num,den))