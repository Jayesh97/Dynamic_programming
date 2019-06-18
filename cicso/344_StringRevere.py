a = ["h","e","l","l","o"]
start = 0
end = len(a)-1
def reverse(a,start,end):
    while start<end:
        temp = a[start]
        a[start] = a[end]
        a[end]=temp
        start=start+1
        end = end-1
reverse(a,start,end)
print(a)