s = "3[a]2[bc2[a]]"
def decodestrings(s):
    stack = []
    stack.append(["",1])
    num = ""
    for ch in s:
        if ch.isdigit():#adding 34 "3"+"4"
            num = num + ch
        elif ch == "[":
            stack.append(["",int(num)])
            num = ""
        elif ch == "]":
            st,count = stack.pop()
            stack[-1][0]=stack[-1][0]+st*count #adding to the previous closed stack
        else: #characters "abc" goes here
            stack[-1][0]=stack[-1][0]+ch
        #print(ch,stack)
    return stack[0][0]
print(decodestrings(s))