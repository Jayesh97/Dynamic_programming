s = "aa"
p = ""
def matching(s,p):
    s_cur = 0
    p_cur = 0
    last_match = 0
    star = -1
    while s_cur<len(s):
        if p_cur<len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=="?"):
            p_cur = p_cur + 1
            s_cur = s_cur + 1
        elif p_cur<len(p) and p[p_cur]=="*":
            last_match = s_cur
            star = p_cur
            p_cur = p_cur+1
        elif(star!=-1):
            p_cur = star+1
            last_match = last_match + 1
            s_cur = last_match
        else:
            return False
    while p_cur<len(p) and p[p_cur]=="*":
        p_cur = p_cur+1
    if p_cur==len(p):
        return True
    else:
        return False

print(matching(s,p))
        
