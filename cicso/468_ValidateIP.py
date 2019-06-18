a = "172.16.a.01"
a = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

a = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
def validate(a):
    l4 = a.split(".")
    l6 = a.split(":")
    if len(l4)==4:
        return validate_ipv4(l4)
    elif len(l6)==8:
        return valdate_ipv6(l6)
    else:
        return "Neither"
def validate_ipv4(l):
    print(l)
    for i in l:
        if i=="":
            return "Neither"
        if not i.isdigit():
            return "Neither"
        if int(i)>255:
            return "Neither"
        if i.startswith('0') and len(i)>1:
            return "Neither"
    return "ipv4"
def valdate_ipv6(l):
    print(l)
    for i in l:
        if i=="":
            return "Neither"
        if len(i)>4:
            return "Neither"
        for val in i:
            if (val >= 'a' and val <= 'f') or (val >= 'A' and val <= 'F') or (val >= '0' and val <= '9'):
                continue
            else:
                return "Neither"
    return "ipv6"
print(validate(a))