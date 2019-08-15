s = "ababcbacadefegdehijhklij"
def partition_labels(s):
    last = {c:i for i,c in enumerate(s)}
    j = anchor = 0
    ans = []
    for i,c in enumerate(s):
        j = max(j,last[c])
        if i==j:
            ans.append(i+1-anchor)
            anchor = i+1
    return ans
print(partition_labels(s))
