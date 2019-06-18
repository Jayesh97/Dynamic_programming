#O(nlgn)
s = "anagram"
t = "nagaram"
def anagram(s,t):
    s = sorted(s)
    t = sorted(t)
    if s==t:
        return True
    return False
print(anagram(s,t))

#O(n)
def anagram2(s,t):
    l = [0 for i in range(26)]
    for i in s:
        l[ord(i)-ord('a')] += 1
    for i in t:
        l[ord(i)-ord('a')] -= 1
    for i in l:
        if i != 0:
            return False
    return True
print(anagram2(s,t))
