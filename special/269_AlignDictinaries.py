words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
def align(words):
    pair_mappings = [] #we--as w>e, er--as e>r
    #i+1 goes for last word
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        for j in range(min(len(word1),len(word2))):
            a = word1[j]
            b = word2[j]
            #pairing of priorities, a has lower priority, b has higher priority
            if a!=b:
                pair_mappings.append(a+b)
                break
    chars = set(''.join(words)) #all unique characters
    order = []
    while pair_mappings:
      #most_prio_ele gives out the most priority element (rtwef - fetr(1st letters))
      most_priority_ele = chars - {pair[1] for pair in pair_mappings}
      if most_priority_ele==set():
        return ""
      order.extend(most_priority_ele)
      chars = chars - most_priority_ele
      #print(most_prio_ele,pair_mappings)
      #most_prio_ele is a set and pair_mappings is an array
      pair_mappings = [pair for pair in pair_mappings if most_priority_ele.isdisjoint(pair)]
    return "".join(order+list(chars))
print(align(words))