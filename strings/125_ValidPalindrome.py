s = "A man, a plan, a canal: Panama"
def valid(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s==s[::-1]
print(valid(s))

s = "A man, a plan, a canal: Panama"
def valid2(s):
    head = 0
    tail = len(s)-1
    while head<tail:
        if s[head].isalnum() and s[tail].isalnum():
            if s[head].lower()==s[tail].lower():
                head = head+1
                tail = tail-1
            else:
                return False
        if s[head].isalnum() == False:
            head = head+1
        if s[tail].isalnum()==False:
            tail = tail-1
    return True
print(valid2(s))