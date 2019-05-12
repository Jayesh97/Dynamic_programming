class Solution(object):
    def diStringMatch(self, a):
        l=[]
        high = len(a)
        low = 0
        for i in a:
            if i == 'D':
                l.append(high)
                high=high-1
            elif i=='I':
                l.append(low)
                low = low+1
        l.append(low)
        return l
s = Solution()
print(s.diStringMatch("DDI"))
        