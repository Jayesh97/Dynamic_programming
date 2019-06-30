A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
def fsum(A,B,C,D):
    di = {}
    total = 0
    for a  in A:
        for b in B:
            s1 = a+b
            if s1 not in di:
                di[s1] = 1
            else:
                di[s1] = di[s1]+1
    print(di)
    for c in C:
        for d in D:
            if -(c+d) in di:
                total = total + di[-(c+d)]   
    return total

print(fsum(A,B,C,D))