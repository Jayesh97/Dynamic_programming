def two_sum(num,sum):
    for i,j in enumerate(num):
        if j in d.values():
            p = num.index(sum-j)
            return (p,i)
        d[i] = sum-j

num = [2,7,11,15,6]
sum = 8
d = {}
t = two_sum(num,sum)
print(t)