height = [0,1,0,2,1,0,1,3,2,1,2,1]
def trap(height):
    total = 0
    left = 0
    right = len(height)-1
    leftmax=0
    rightmax = 0
    while left<right:
        if height[left]<height[right]:
            if height[left]>=leftmax:
                leftmax = height[left]
            else:
                total = total+leftmax-height[left]
            left = left+1
        else:
            if height[right]>=rightmax:
                rightmax = height[right]
            else:
                total = total+rightmax-height[right]
            right = right-1
    return total
print(trap(height))