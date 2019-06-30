nums = [3,30,34,5,9]

class comp(str):
    def __lt__(x,y):
        return x+y>y+x

def large(nums):
    return "".join(sorted(map(str,nums),key=comp))

def largest(nums):
        l = len(str(max(nums)))+1
        nums = map(str,nums)
        weight = []
        ans = []
        for i in nums:
            weight.append(((i*l)[:l],i))
        weight.sort(reverse=True)
        for i in weight:
            ans.append(i[1])
        return "".join(ans)

print(large(nums))
print(largest(nums))