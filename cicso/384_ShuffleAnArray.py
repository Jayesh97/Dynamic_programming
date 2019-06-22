import random
class Solution(object):
    def __init__(self, nums):
        self.array = nums
        self.orginal = list(nums)
        
    def reset(self):
        self.array = list(self.orginal)
        return self.array
        
    def shuffle(self):
        temp =  list(self.array)
        for i in range(len(self.array)):
            remove_i = random.randrange(len(temp))
            self.array[i]= temp.pop(remove_i)
        return self.array
        
nums = [1,2,3,4,5,6,7]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
print(obj.reset())

class Solution2(object):
    def __init__(self, nums):
        self.array = nums
        self.orginal = list(nums)
        
    def reset(self):
        self.array = list(self.orginal)
        return self.array
        
    def shuffle(self):
        for i in range(len(self.array)):
            swap_i = random.randrange(i,len(self.array))
            self.array[i],self.array[swap_i]= self.array[swap_i],self.array[i]
        return self.array

nums2 = [1,2,3,4,5,6,7,8,9]
obj2 = Solution(nums2)
param_1 = obj2.reset()
print(param_1)
param_2 = obj2.shuffle()
print(param_2)
print(obj2.reset())