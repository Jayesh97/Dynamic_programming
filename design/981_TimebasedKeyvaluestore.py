from collections import defaultdict
class Timestamp(object):
    def __init__(self):
        self.d = defaultdict(list)

    def set(self,key,value,timestamp):
        self.d[key].append([timestamp,value])

    def get(self,key,timestamp):
        arr = self.d[key]  #[[t1,v1],[t2,v2],[t3,v3]]
        n = len(arr)
        left,right = 0,n
        while left<right:
            mid = (left+right)//2
            if arr[mid][0]==timestamp:
                return arr[mid][1]
            elif arr[mid][0]<timestamp:
                left = mid+1
            else:
                right=mid
        return "" if right==0 else arr[right-1][1]

obj = Timestamp()
obj.set("foo","bar",1)
print(obj.get("foo",1))


