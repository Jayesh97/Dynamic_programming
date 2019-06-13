#Dynamic programming
a = [2,3,1,1,2,4,2,0,1,1]
t = [0 for i in range(len(a))]
for i in range(1,len(a)):
    t[i] = float('inf')
    for j in range(0,i):
        if i<=j+a[j]:
            t[i] = min(t[i],t[j]+1)
print(t[-1])

'''
Greedy
farthest = 0
jump = 0
end_range = 0  --- used to determine the jump that could expire here
'''
def jump_g(a):
    farthest = 0
    jump = 0
    end_range = 0
    for i,j in enumerate(a[:-1]):
        if i+j>farthest:
            farthest = i+j
        if farthest>=len(a)-1:
            return jump+1
        if i==end_range:
            jump = jump+1
            end_range = farthest
    return jump

print(jump_g(a))


