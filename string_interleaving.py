'''
Checking truth values with the substring
'''
def matrix(x,y,s1,s2,s3):
    k = [[0 for i in range(x+1)] for j in range(y+1)]
    for y in range(y+1):
        for x in range(x+1):
            if x==0 and y==0:
                k[x][y] = 1
            elif x==0:
                if k[x][y-1] == 1 and s3[y-1]==s1[y-1]:
                    k[x][y] = 1
            elif y==0:
                if k[x-1][y] == 1 and s3[x-1]==s2[x-1]:
                    k[x][y] = 1
            else:
                if (k[x][y-1] == 1 and s3[x+y-1]==s1[y-1]) or (k[x-1][y] and s3[x+y-1]==s2[x-1]):
                    k[x][y] = 1
    return k


string1 = "aab"
string2 = "axy"
string3 = "aaxaby"
x = len(string2)
y = len(string1)
mat = matrix(x,y,string1,string2,string3)
print(mat)
if mat[x][y] == 1:
    print("True")
else:
    print("False")