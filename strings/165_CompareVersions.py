version1 = "01"
version2 = "1"
def version(version1,version2):
    v1,v2 = (map(int,v.split('.')) for v in (version1,version2))
    v1 ,v2= [i for i in v1],[j for j in v2]
    #print(v1,v2)
    d = len(v2)-len(v1)
    if v1+[0]*d>v2+[0]*-d:
        return 1
    elif v1+[0]*d==v2+[0]*-d:
        return 0
    return -1

    
print(version(version1,version2))