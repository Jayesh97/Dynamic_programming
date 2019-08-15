from collections import Counter
s = "ABABCAABCB"
k = 2
def characterReplacement(s, k):
    res = lo = hi = 0
    counts = Counter()
    for hi in range(1, len(s)+1):
        counts[s[hi-1]] += 1
        max_char_n = counts.most_common(1)[0][1]
        print(max_char_n,hi,lo)
        #high-lo-max_char acts as a sliding window and it increases only if the new_maxx exceeds the overall maxx
        if hi - lo - max_char_n > k:
            counts[s[lo]] -= 1
            lo += 1
        print(max_char_n,hi,lo)
    return hi - lo
print(characterReplacement(s,k))