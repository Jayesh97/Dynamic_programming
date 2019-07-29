s = "aa"
p = "a*"

def matching(s,p):
    if not p:
        #print(s,p)
        return not s
    #like "aa" and ".*"
    if s!="" and p[0] in (s[0],'.'):
        firstmatch = True
    else:
        firstmatch = False
    #print(firstmatch)
    #for those with "aa" and "c*aa"
    #1st letter doesnt match but 2nd letter has a *
    if len(p)>1 and p[1]=="*":
        #c*aa case and aaaaabb and a*bb case
        return matching(s,p[2:]) or (firstmatch and matching(s[1:],p))
    #if there is 1st match "aa" and "ab" or "aa" and "ca" --- even no match can go here
    else:
        return firstmatch and matching(s[1:],p[1:])

print(matching(s,p))

s = "aa"
p = "a*"

#DP - Top Down approach
def dpmatching(s,p):
    cache = {}
    def dp(i,j):
        if (i,j) not in cache:
            if j==len(p):
                if i==len(s):
                    ans=True
                else:
                    ans=False
            else:
                #checking for a match 
                if i<len(s) and p[j] in (s[i],'.'):
                    firstmatch = True
                else:
                    firstmatch = False
                #for c* or .*
                if j+1<len(p) and p[j+1]=="*":
                    ans = dp(i,j+2) or (firstmatch and dp(i+1,j))
                else:
                    ans = firstmatch and dp(i+1,j+1)
            cache[i,j]=ans
        return cache[i,j]
    return dp(0,0)     
            
print(dpmatching(s,p))

