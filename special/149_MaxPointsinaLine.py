points = [[1,1],[2,2],[3,3],[1,1]]
def maxpoints(points):
    if len(points)<3:
        return len(points)
    res = 0
    for i in range(len(points)-1):
        cur = 0
        overlap = 0
        lines = {}
        for j in range(i+1,len(points)):
            #print(points[i],points[j])
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            if dx==dy==0:
                overlap =overlap+1
                continue
            key = None if dx==0 else 1.0*dy/dx
            #print(lines)
            lines[key]=lines.get(key,0)+1
            cur = max(cur,lines[key])
        #print(lines,cur,overlap)
        res=max(res,cur+overlap)
        #print(res)
    return res+1

print(maxpoints(points))