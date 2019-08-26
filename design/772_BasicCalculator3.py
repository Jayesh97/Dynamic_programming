s = "2*(5+5*2)/3+(6/2+8)"
s = "5-3/2"
def calculate(s):
    def stack_update(op,num):
        if op=="+":
            stack.append(num)
        elif op=="-":
            stack.append(-num)
        elif op=="*":
            stack.append(stack.pop()*num)
        elif op=="/":
            if stack[-1]<0  :
                stack.append(stack.pop()//num+1)
            else:
                stack.append(stack.pop()//num)
    stack=[]
    num,op=0,"+"
    for i in s:
        if i.isdigit():
            num=num*10+int(i)
        elif i in "+*-/)":
            stack_update(op,num)
            if i==")":
                num=0
                while stack!=None and isinstance(stack[-1],int):
                    num = num+stack.pop()
                op=stack.pop()
                stack_update(op,num)
            num,op=0,i
        elif i=="(":
            stack.append(op)
            num,op=0,"+"
    stack_update(op,num)
    return sum(stack)

print(calculate(s))
        