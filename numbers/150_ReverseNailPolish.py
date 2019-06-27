tokens  = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
def stackify(tokens):
    stack = []
    for i in tokens:
        if i == "+" or i=="-" or i=="*" or i=="/":
            num2 = stack.pop()
            num1 = stack.pop()
            sign = i
            result = evaluate(int(num1),int(num2),sign)
            stack.append(result)
        else:
            stack.append(i)
    return stack[0]

def evaluate(num1,num2,sign):
    if sign == "+":
        return num1+num2
    if sign == "-":
        return num1-num2
    if sign == "*":
        return num1*num2
    if sign == "/":
        if num1*num2 < 0:
            num1 = abs(num1)
            num2 = abs(num2)
            sign = -1
            result = num1/num2
            return result*sign
        return num1/num2

print(stackify(tokens))