#print(3 << 4)
a = 15
b = 3
sign = -1 if a<0 or b<0 else 1
a = abs(a)
b = abs(b)
q = 0
summ = 0
for i in range(31,-1,-1):
    if (summ + b<<i <= a):  #b<<i - 12 which is less than 20
        summ = summ + b<<i
        #print(summ,i)
        q = q | 1<<i
print(q)