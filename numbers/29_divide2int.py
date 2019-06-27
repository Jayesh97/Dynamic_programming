#print(3 << 4)
dividend = 15
divisor = 3
def divide(dividend,divisor):
        sign = -1 if dividend<0 or divisor<0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend>=divisor:
                temp = divisor
                i = 1
                while dividend>=temp:
                        dividend = dividend-temp
                        quotient = quotient+i
                        temp = temp <<1
                        i = i<<1
        return quotient*sign
print(divide(dividend,divisor))