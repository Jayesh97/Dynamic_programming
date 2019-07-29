s = "IXX"
def romantoint(s):
    roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    total = 0
    for i in range(len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            total = total - roman[s[i]]
        else:
            total = total + roman[s[i]]
    total = total + roman[s[-1]]
    return total
print(romantoint(s))

