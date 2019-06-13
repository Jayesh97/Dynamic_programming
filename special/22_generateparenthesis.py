def parenthesis(string,n,current,openn,close):
    if close == n:
        l = []
        for i in string:
            l.append(i)
        s = "".join(l)
        d.append(s)
    else:
        if openn>close:
            string[current]=')'
            parenthesis(string,n,current+1,openn,close+1)
            #2,
        if openn<n:
            string[current]='('
            parenthesis(string,n,current+1,openn+1,close)
            #1,3
n = 3
string = [""]*2*n #n open + n close - total 2*n
current = 0
openn = 0
close = 0
d = []
parenthesis(string,n,0,0,0)
print(d)