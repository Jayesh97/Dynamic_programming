import heapq
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
def topkfreq(words,k):
    d = {}
    #o(n)
    for i in words:
        d[i]=d.get(i,0)+1
    heap = [(-freq,word) for word,freq in d.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for i in range(k)]
print(topkfreq(words,k))