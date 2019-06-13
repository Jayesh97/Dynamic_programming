a = ['a','b','c']
n = len(a)
d = []
for i in range(1<<n):
    l = []
    for j in range(n):
        if (i & (1<<j)) > 0:
            l.append(a[j])
    d.append(l)
print(d)

""" 
password issue for docker - Rag1994&

vcl - no root - /home/<id>/.bashrc

exit and open again for changes

needed to modify the utility.py

read - giving out the json file

utilities.py - line 41 - replace ip with varfile at the input to file object

update is not working
"""
