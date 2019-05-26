num = [1,2,3,4,5,6,7]
k = 4
def rotate(num,k):
    a = [0 for x in range(len(num))]
    for i in range(len(num)):
        a[(i+k)%len(num)] = num[i]
    print(a)
    
def rotate_reverse(num,k):
    k = k % len(num)
    reverse(num,0,len(num)-1)
    reverse(num,0,k-1)
    reverse(num,k,len(num)-1)
    print(num)
def reverse(num,start,end):
    while start<end:
        temp = num[start]
        num[start] = num[end]
        num[end] = temp
        start = start+1
        end = end-1

rotate(num,k)
rotate_reverse(num,k)
