#swapping 1st and last
a = [1,2,3,4,5,6]
def reverse(a,k):
    for i in range(k/2):
        temp = a[i]
        a[i] = a[k-i-1]
        a[k-i-1] = temp
    return a
print(reverse(a,4))


#using list indices
a = [1,2,3,4,5,6]
n = 4
a = a[n-1::-1]+a[n:]
print(a)