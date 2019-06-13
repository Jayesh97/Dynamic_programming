stack = []
d = {')':'(','}':'{',']':'['}
string = "{[]}[]}"
def validation(string):
    for i in string:
        if i in d.values(): #openings go here
            stack.append(i)
        else: #closing or invalid go here
            if i in d.keys():
                if stack==[]:
                    return False 
                if stack[-1]==d[i]: 
                    stack.pop()
                else:
                    return False #wrong closings
            else:
                return False
        #print(stack)
    if stack == []: 
        return True
    return False
print(validation(string))