import random
points = [[1,3],[-2,2],[2,5],[-1,-1]]
k = 1
dist = lambda i:points[i][0]**2+points[i][1]**2
def q_sort(i,j,k):
    if i>=j:
        return
    #Choice of random pivot guarantees of the worst case O(n)
    p=random.randint(i,j)
    print(p)
    points[i],points[p]=points[p],points[i] #selects a random pivot and swaps with 1st element
    midd = partition(i,j)
    print(midd) #finds the proper position of pivot
    print(points)
    if k<midd-i+1:
        q_sort(i,midd-1,k)
    elif k>midd-1+1:
        q_sort(midd+1,j,k-(midd-i+1))
def partition(i,j):
    start = i
    pivot = dist(i)
    i=i+1
    while True:
        while i<j and dist(i)<pivot:
            i=i+1
        while i<=j and dist(j)>=pivot:
            j=j-1
        if i>=j:
            break
        points[i],points[j]=points[j],points[i]
    points[start],points[j]=points[j],points[start]
    return j
q_sort(0,len(points)-1,k)
print(points[:k])