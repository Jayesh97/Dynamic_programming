from collections import defaultdict
n = 4
courses  =  [[1,0],[2,0],[3,1],[3,2]]
def schedule(courses,n):
    d = defaultdict(list)
    degree = {}
    for pre_req,course in courses:
        d[course].append(pre_req)
        degree[pre_req]=degree.get(pre_req,0)+1
    zero_degree_queue = [i for i in range(n) if i not in degree]
    topologial_order = []
    #print(zero_degree_queue)
    while zero_degree_queue:
        current = zero_degree_queue.pop(0)
        topologial_order.append(current)
        #print(topologial_order)
        if current in d:
            for i in d[current]:
                degree[i] = degree[i]-1
                if degree[i]==0:
                    zero_degree_queue.append(i)
    return topologial_order if len(topologial_order)==n else []
print(schedule(courses,n))