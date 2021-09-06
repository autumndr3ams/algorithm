import heapq

def changeheap(heap):
    newh = []
    for n in heap:
        heapq.heappush(newh, -n)
    return newh

def solution(operations):
    minheap = []
    maxheap = []
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        
        if op=="I":
            heapq.heappush(minheap, n)
            heapq.heappush(maxheap, -n)
        elif minheap and maxheap:
            if n < 0:
                heapq.heappop(minheap)
                maxheap = changeheap(minheap)
            else:
                heapq.heappop(maxheap)
                minheap = changeheap(maxheap)
    if minheap and maxheap:
        answer = [-maxheap[0], minheap[0]]
    else:
        answer = [0, 0]
    return answer