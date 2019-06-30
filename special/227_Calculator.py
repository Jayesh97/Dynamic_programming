s = "14-3/2"
def calculate(s):
    num = 0
    sign = "+"
    stack = []
    for j,i in enumerate(s):
        if i.isdigit():
            num = num*10+int(i)
        if i in ["+","-","/","*"] or j==len(s)-1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                last = stack.pop()
                stack.append(num*last)
            else:
                print(stack)
                last = stack.pop()
                if last<0:
                    stack.append((last/num)+1)
                else:
                    stack.append(int(last/num))
            num=0
            sign=i
    return sum(stack)

print(calculate(s))