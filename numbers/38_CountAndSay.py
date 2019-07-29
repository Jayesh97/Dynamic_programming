n = 3
def countandsay(n):
    result = "1"
    for i in range(n-1):
        prev = result
        result = ""
        j = 0
        while j<len(prev):
            current = prev[j]
            count = 1
            j = j+1
            #if the next character also repeats, we need to increase count
            #So this inner loop
            while j<len(prev) and prev[j]==current:
                count = count+1
                j = j+1
            result = result + str(count)+str(current)
    return result
print(countandsay(3))



print(countandsay(n))