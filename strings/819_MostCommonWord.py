paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
def most_common(paragraph,banned):
    d = {}
    for c in "?,./;!":
        paragraph = paragraph.replace(c," ")
    for i in paragraph.lower().split():
        d[i]=d.get(i,0)+1
    most_freq,maxx='',0
    #print(d)
    for word in d:
        if d[word]>maxx and word not in banned:
            most_freq,maxx=word,d[word]
    return most_freq
print(most_common(paragraph,banned))