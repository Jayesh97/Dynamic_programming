class Solution(object):
    def numJewelsInStones(self, J, S):
        d = {}
        count=0
        for i in J:
            if i not in d:
                d[i] = 1
        for i in S:
            if i in d:
                count=count+1
        return count
    
val=Solution()
print(val.numJewelsInStones('a','Aaa'))