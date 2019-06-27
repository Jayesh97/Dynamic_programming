from collections import defaultdict
def anagrams(strs):
    result = defaultdict(list)
    for i in strs:
        count = [0]*26
        for char in i:
            count[ord(char)-ord('a')]+=1
        result[tuple(count)].append(i)
    return result.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagrams(strs))