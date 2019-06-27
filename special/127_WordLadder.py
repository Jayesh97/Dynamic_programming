from collections import defaultdict
import string
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"
def ladder(wordList,beginWord,endWord):
    if not wordList or not beginWord or not endWord or endWord not in wordList:
        return 0
    n = len(beginWord)
    queue = [(beginWord,1)]
    visited = set([beginWord])
    wordList = set(wordList)
    while queue:
        current,level = queue.pop(0)
        for i in range(n):
            for letter in string.ascii_lowercase:
                new_word = current[:i]+letter+current[i+1:]
                if new_word == endWord:
                    return level+1
                elif new_word in wordList and new_word not in visited:
                    queue.append((new_word,level+1))
                    visited.add(new_word)
    return 0

print(ladder(wordList,beginWord,endWord))