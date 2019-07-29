logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
def func(log):
    #splits into 2 words at 1st occurance of the " "
    idc,rest = log.split(" ",1)
    return  (0,rest,idc) if rest[0].isalpha() else (1,)
print(sorted(logs,key=func))