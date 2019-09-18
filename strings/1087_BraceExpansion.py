s = "{a,b,c}d{e,f}"
res = []
def braceexpansion(s,word,location): #location keeps track of all } 
    if not s:
        #print(res)
        res.append(word)
    elif s[0]=="{":  #runs till u get }
        #print(s)
        for i in range(len(s)):
            if s[i]=="}":
                location = i
                break
        #i = s.find("}")
        #print(i)
        for char in s[1:location].split(','):
            braceexpansion(s[location+1:],word+char,location+1)
    else:
        braceexpansion(s[1:],word+s[0],location+1) 
    res.sort()
    return res

print(braceexpansion(s,"",0))
