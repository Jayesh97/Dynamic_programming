#floyds method
a = [1,4,6,6,6,2,3]
p1 = a[0]
p2 = a[0]
while True:
    p1 = a[p1]
    p2 = a[a[p2]]
    if p1 == p2:
        break

ptr1 = a[0]
ptr2 = p1
while ptr1!=ptr2:
    ptr1 = a[ptr1]
    ptr2 = a[ptr2]
print(ptr1)

#using set
s = set()
for i in a:
    if i in s:
        print(i)
        break
    else:
        s.add(i)


#using abs values, prints all repeating elements
a = [1, 2, 3, 1, 3, 6, 6] 
for i in a:
    if a[abs(i)] >= 0:
        a[abs(i)] = -a[abs(i)]
    else:
        print(abs(i))