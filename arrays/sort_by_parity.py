class Solution(object):
    def sortArrayByParity(self, a):
        #a.sort(key=lambda x:x%2)
        j=0
        for i in range(len(a)):
            if a[i]%2==0:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                j=j+1
        return a
t = Solution()
val = t.sortArrayByParity([3,1,2,4])
print(val)