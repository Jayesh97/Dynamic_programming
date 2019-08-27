n = 123
def inttoeng(num):
    def one(num):
        d = {1: 'One',2: 'Two',3: 'Three',4: 'Four',5: 'Five',6: 'Six',7: 'Seven',8: 'Eight',9: 'Nine'}
        return d.get(num)
    def twostwenty(num):
        d = {10: 'Ten',11: 'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18: 'Eighteen',19: 'Nineteen'}
        return d.get(num)
    def tens(num):
        d = {2: 'Twenty',3: 'Thirty',4: 'Forty',5: 'Fifty',6: 'Sixty',7: 'Seventy',8: 'Eighty',9: 'Ninety'}
        return d.get(num)
    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
    def two(num):
        if not num:
            return ""
        elif num<10:
            return one(num)
        elif num<20:
            return twostwenty(num)
        else:
            tenner = num//10
            rest=num-tenner*10
            return tens(tenner)+" "+one(rest) if rest else ten(tenner)
    def three(num):
        hundred=num//100
        rest=num-hundred*100
        if hundred and rest:
            return one(hundred)+" Hundred "+two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred)+" hundred"
        
    if not num:
        return "zero"
    result = ""
    if billion:
        result = three(billion)+"billion"
    if million:
        result = result + " " if result else ""
        result = result + three(million)+"million"
    if thousand:
        result = result + " " if result else ""
        result = result + three(thousand)+"thousand"
    if rest:
        result = result + " " if result else ""
        result = result + three(rest)
    return result


print(inttoeng(n))