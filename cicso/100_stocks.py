a = [7,1,5,3,6,4]
least = float('inf')
maxx = 0
for i in a:
    if i<least:
        least = i
    profit = i-least
    if profit>maxx:
        maxx = profit
print(maxx)
