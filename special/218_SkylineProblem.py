from heapq import heappop,heappush

buildings = [ [2,9,10], [3, 7 ,15], [5, 12, 12], [15, 20 ,10], [19, 24 ,8] ]

def skyline(buildings):

    #Possible corner positions
    position = sorted(set([building[0] for building in buildings]+[building[1] for building in buildings]))
    #print(position)
    sky = [[-1,0]]
    coverage = [] #has the heightest height as -h at postion 0
    i = 0

    for axis in position:
        #Add new building whose left overshadows position t
        while i<len(buildings) and buildings[i][0]<=axis:
            heappush(coverage,(-buildings[i][2],buildings[i][1]))
            i = i+1
        #remove buildings whose rightside has no significance
        while coverage and coverage[0][1]<=axis:
            heappop(coverage)

        h = -coverage[0][0] if coverage else 0
        if sky[-1][1]!=h:
            sky.append([axis,h])
        #print(coverage,"coverage",t)
        #print(sky,"sky")
    return sky[1:]


print(skyline(buildings))