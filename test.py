def reorder(logs):
    def func(log):
        #splits into 2 words at 1st occurance of the " "
        idc,rest = log.split(" ",1)
        return  (0,rest,idc) if rest[0].isalpha() else (1,)
    return sorted(logs,key=func)
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorder(logs))