s = "aab"
def palin(s):
    n = len(s)
    if n==0:
        return [[]]
    total = [[s[0]]]
    for i in range(1,n):
        len_total = len(total)
        for j in range(len_total):
            print(s[i])
            current = total[j]
            if current[-1]==s[i]:
                temp = list(current)
                temp[-1]=temp[-1]+s[i]
                total.append(temp)
                print(s[i],current,temp,total,"1")
            if len(current)>1 and current[-2]==s[i]:
                temp = list(current[:-2])
                temp.append(''.join(current[-2:]+[s[i]]))
                total.append(temp)
                print(s[i],current,total,"2")
            current.append(s[i])
    return total
print(palin(s))
