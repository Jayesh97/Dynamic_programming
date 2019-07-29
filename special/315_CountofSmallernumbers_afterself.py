nums = [9,2,6,1]
def merge_sort(enums):
    half = int(len(enums)/2)
    print(half)
    if half>0:
        left,right = merge_sort(enums[:half]),merge_sort(enums[half:])
        for i in range(len(enums))[::-1]:
            #print(i,left,right,enums)
            if not right or left and left[-1][1]>right[-1][1]:
                smaller[left[-1][0]]=smaller[left[-1][0]]+len(right)
                enums[i]=left.pop()
            else:
                enums[i]=right.pop()
            #print(enums)
    return enums

smaller = [0]*len(nums)
enums = list(enumerate(nums))
print(merge_sort(enums))
print(smaller)