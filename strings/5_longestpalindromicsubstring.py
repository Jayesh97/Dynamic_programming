class Solution(object):
    def longestPalindrome(self, s):
        start = 0
        end = 0
        def expand(s,left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left=left-1
                right=right+1
            return right-left-1
        for i in range(len(s)):
            print(i)
            l1 = expand(s,i,i)
            l2 = expand(s,i,i+1)
            l = max(l1,l2)
            if l>end-start:
                start = i-(l-1)/2
                end = i+l/2
        return s[start:end+1]
sub = Solution()
print(sub.longestPalindrome("babad"))