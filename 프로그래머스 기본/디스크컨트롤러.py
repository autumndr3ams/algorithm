import heapq

def solution(jobs):
    answer = 0
    count, start, now = 0, -1, 0
    q = []
    length = len(jobs)
    
    while count < len(jobs):
        for job in jobs:
            if start<job[0]<=now:
                heapq.heappush(q, [job[1], job[0]])
        if q:
            cur = heapq.heappop(q)
            start = now
            now += cur[0]
            answer += (now-cur[1])
            count+=1
        else:
            now+=1
    return int(answer/length)