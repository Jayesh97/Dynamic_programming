heigth = [2,1,5,6,2,3]
def rec_area(heigth):
    heigth.append(0)
    stack = [-1] #absolute position of width from origin
    ans = 0
    for i in range(len(heigth)):
        while heigth[i]<heigth[stack[-1]]:#stack[-1] = -1 initially and h[-1]=0 ==> leads to false
            #print(stack)
            h = heigth[stack.pop()]
            w = i-stack[-1]-1 #width from ith element
            #print(h,w) #w represents the max width possible for that certain height
            ans = max(ans,h*w)
        stack.append(i)
    return ans


print(rec_area(heigth))