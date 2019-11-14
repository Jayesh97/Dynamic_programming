input = """network-services,DNS\n
name,luv\n
Name,jayesh\n
Network-services,DHCP"""
l = input.strip(" ").split("\n")
print(l)
l = set(l)
if "" in l:
    l.remove("")
d = {}
print(l)
for i in l:
    key,valuen = i
    key,value = key.lower(),value
    d[key]=d.get(key,[])
    d[key].append(value)
    """
    if key in d:
        d[key].append(value)
    else:
        d[key]=[value]
    """
print(d)
