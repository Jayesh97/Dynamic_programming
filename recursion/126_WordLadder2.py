import string
from collections import defaultdict
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
def wordladder2(beginWord,endWord,wordList):
    wordList = set(wordList)
    res = []
    d = {}
    d[beginWord]=[[beginWord]]
    print(d)
    while d:
        new_d = defaultdict(list)
        for word in d.keys():
            print(word)
            if word==endWord:
                res.extend(i for i in d[word]) # i will be a list as d[word] is a list of list
            else:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i]+c+word[i+1:]
                        if new_word in wordList:
                            new_d[new_word]=new_d[new_word]+[j+[new_word] for j in d[word]]
                            print(new_d)
        wordList=wordList-set(new_d.keys())
        d = new_d
        print(d,"updated")
    return res
print(wordladder2(beginWord,endWord,wordList))


