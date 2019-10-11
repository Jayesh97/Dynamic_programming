import re

s = "sd00dasdsd000ddd \n d00000dsd"
#s = s.replace("\n"," ")
l = re.findall(r"d0+ddd$",s)  #end of the line
print(l)
l = re.match(r".*(d0.*dsd)",s)  #doesnt match new lines
print(l.groups())
l = re.findall(r"d0+dsd$",s)
print(l)

s = "the cat \nThe dog \ntell me \n count" #using space after a char considers as /s
l = re.findall(r'^tell',s) #matches only the 1st line 1st word
print(l)    
l = re.findall(r'(^[Tt].*)\s?.*',s,re.MULTILINE)
print(l)

s = "1000111100001100101"
l = re.findall(r"10{2,4}1",s) #matches 0 which occurs 2-4 times
print(l)

s = "jayesh5399@gmail.com, cat@dmai.com, this is the cost of sjbondu@ncsu.edu"
l = re.findall(r'\w+@\w+\.\w+',s)
print(l)

s = "teLL"
l = re.findall("tell",s,re.I)
print(l)