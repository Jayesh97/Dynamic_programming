a = [1, 2, 4 , 6, 3, 7, 8]

#using total
n = len(a)+1
total = (n)*(n+1)/2
for i in a:
    total = total - i
print(total)

#using xor
total1 = 0
total2 = 0
for i in a:
    total1 = total1 ^ i
for i in range(1,len(a)+2):
    total2 = total2 ^ i
t = total1 ^ total2
print(t)
