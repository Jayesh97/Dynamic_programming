import random

class RandomSet(object):

    def __init__(self):
        self.nums , self.pos = [],{}

    def insert(self,val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val]=len(self.nums)-1 #Index of the word in nums  - len(nums)
            return True
        return False

    def remove(self,val):

        if val not in self.pos:
            return False
        index = self.pos[val]
        last = self.nums[-1]
        self.nums[index] = last #replacing apple with cat; now apple is not present
        self.pos[last] = index #changing position of cat to apple
        self.nums.pop() #removing cat as cat moved to apple
        self.pos.pop(val,0)
        return True

    def getRandom(self):

        return self.nums[random.randint(0,len(self.nums)-1)]


ob = RandomSet()
ob.insert(1)