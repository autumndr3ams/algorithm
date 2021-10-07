import heapq
def solution(n, works):
    answer = 0
    if sum(works)<=n: return 0
    
    heap = []
    for i in works:
        heapq.heappush(heap, -i) #최대힙 
        
    while n:
        tmp = abs(heapq.heappop(heap))
        heapq.heappush(heap, (tmp-1)*(-1))
        n-=1
        
    return sum([i*i for i in heap])