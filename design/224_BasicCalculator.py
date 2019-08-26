s = "(1+(4+5+2)-3)+(6+8)"
def calculator(s):
    def stack_update(op,num):
        if op=="+":
            stack.append(num)
        elif op=="-":
            stack.append(-num)
    stack=[]
    num,op=0,"+"
    for i in s:
        if i.isdigit():
            num=num*10+int(i)
        elif i in "+-)":
            stack_update(op,num)
            if i==")":
                num=0
                #add all numbers until u get a sign
                while stack!=[] and isinstance(stack[-1],int):
                    num = num+stack.pop()
                op=stack.pop()
                stack_update(op,num)
            num,op=0,i
        #if there is - before () we append - to stack
        elif i=="(":
            stack.append(op)
            num,op=0,"+"
    stack_update(op,num)
    return sum(stack)

print(calculator(s))





