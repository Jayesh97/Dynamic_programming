digits = [9,9]
def plusone(digits):
    if len(digits)==1 and digits[0]==9:
        return [1,0]
    if digits[-1]!=9:
        digits[-1]=digits[-1]+1
        return digits
    else:
        digits[-1]=0
        digits[:-1]=plusone(digits[:-1])
        return digits
print(plusone(digits))