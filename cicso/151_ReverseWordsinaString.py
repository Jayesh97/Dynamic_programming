#Build-ins
s = "  hello   this        world!  "
s = s.strip(" ")
l = s.split(" ")
l = l[::-1]
s = " ".join([i for i in l if len(i)>0])
print(s)

def reverseWords(s):
    space_index = len(s)
    last = len(s) - 1
    reversed_words = ''
    for index in range(last, -1, -1):
        if s[index] == ' ':
            space_index = index
        elif index == 0 or s[index - 1] == ' ':
            if reversed_words: 
                reversed_words += ' '
            word = s[index:space_index]
            reversed_words += word
    return reversed_words

s = "  hello  world  "
print(reverseWords(s))