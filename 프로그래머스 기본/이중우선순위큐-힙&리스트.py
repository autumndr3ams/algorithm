import heapq

def solution(operations):
    q = []
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        
        if op=="I":
            heapq.heappush(q, n)
        elif q:
            if n < 0:
                heapq.heappop(q)
            else:
                q.remove(max(q))
    if q:
        answer = [max(q), q[0]]
    else:
        answer = [0, 0]
    return answer