import collections
import heapq
a = [1,1,1,2,2,3]
n = 2
count = collections.Counter(a)
#print(count)
print(heapq.nlargest(2,count,key=count.get))


#----------Method-2-------------#
a = [1,1,1,2,2,3]
d = {}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i] = d[i]+1
def get_value(x):
    return d[x]
print(heapq.nlargest(2,d,key=get_value))