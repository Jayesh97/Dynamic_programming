a = [[1,3],[8,10],[15,18],[2,6]]
a.sort(key=lambda x: x[0])
merged = []
for i in a:
    if not merged or merged[-1][-1]<i[0]:
        merged.append(i)
    else:
        merged[-1][-1] = i[-1]
print(merged)