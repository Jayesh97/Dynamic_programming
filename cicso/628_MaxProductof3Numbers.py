a = [1,2,3,4,-5,-6]

def prod_3(a):
        max1 = -1001
        max2 = -1001
        max3 = -1001
        min1 = 1001
        min2 = 1001
        for i in a:
            if i>max1:
                max3=max2
                max2=max1
                max1=i
            elif i>max2:
                max2=i
                max3=max2
            elif i>max3:
                max3=i
            if i<min1:
                min2=min1
                min1=i
            elif i<min2:
                min2=i
            #print(max1,max2,max3,min1,min2)
        return max(max1*max2*max3,max1*min1*min2)
print(prod_3(a))