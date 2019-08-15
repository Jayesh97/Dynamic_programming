import heapq
intervals = [[0, 30],[15, 20],[5, 10]]
def meetingrooms(intervals):
    if not intervals:
        return 0
    free_rooms = [] #heap
    intervals.sort(key=lambda x:x[0]) #based on start time
    print(intervals)
    heapq.heappush(free_rooms,intervals[0][1]) #pushing the end time
    print(free_rooms)
    for i in intervals[1:]:
        print(free_rooms)
        if free_rooms[0]<=i[0]:
            heapq.heappop(free_rooms)
        print(free_rooms)
        heapq.heappush(free_rooms,i[1])
    return len(free_rooms)


print(meetingrooms(intervals))