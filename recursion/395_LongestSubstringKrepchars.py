s = "abcabb"
k = 2
def longest(s,k):
    if len(s)<k:
        return 0
    for c in set(s):
        if s.count(c)<k:
            return max(longest(z,k) for z in s.split(c))
    return len(s)

print(longest(s,k)) 