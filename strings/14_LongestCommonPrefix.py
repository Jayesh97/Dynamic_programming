strs = ["flower","flow","flight"]
def longestprefix(strs):
    if len(strs)==0:
        return ""
    prefix = strs[0]
    for i in range(1,len(strs)):
        while prefix not in strs[i][0:len(prefix)]:
            prefix = prefix[:-1]
        if prefix == "":
            return ""
    return prefix
print(longestprefix(strs))
