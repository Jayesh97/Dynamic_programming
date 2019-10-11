s = "ababcbacadefegdehijhklij"
def partition_labels(s):
    last = {c:i for i,c in enumerate(s)}
    print(last)
    j = anchor = 0 #anchor - start and end of current partition, or the split point of partitions
    ans = []
    for i,c in enumerate(s):
        j = max(j,last[c])
        #print(j)
        if i==j:
            ans.append(i+1-anchor)
            anchor = i+1
    return ans
print(partition_labels(s))