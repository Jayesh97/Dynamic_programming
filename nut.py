a = [3,17,4,12,5,6,3,1]

import operator

def findmax(a):
    index, value = max(enumerate(a), key=operator.itemgetter(1))
    return (index,value)

d = {} #mapping peak and deletions


def left(a,index,del_count):
    for i in range(index,0,-1):
        if i==1:
            return del_count
        if a[i-1]>a[i]:
            del_count = del_count + 1
    return del_count
        
def right(a,index,del_count):
    global_max = 0
    i = 0
    while i<len(a)-2:
        if a[i+1]<a[i+2]:
            global_max = max(a[i+2],global_max)
            del_count = del_count + 1
        i=i+1
    return del_count


def count_del(a,del_count):
    if a == sorted(a):
        return 0
    if a == sorted(a,reverse=True):
        return 0
    a1 = a
    index,value = findmax(a)
    del_count = 0
    del_count = left(a,index,del_count)
    del_count = right(a,index,del_count)
    d[index] = del_count
    return(del_count)
    

print(count_del(a,0))



