import heapq

def dijkstra(graph, first, N):
    distance = {node:float('inf') for node in range(N)}
    distance[first] = 0
    queue=[]
    heapq.heappush(queue, [distance[first], first])
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if distance[cur_node] < cur_dist: # 우선순위 큐의 값이 더 클경우 반복문 실행할 필요 없음
            continue
        for next_node, w in graph[cur_node]:
            total_dist = cur_dist + w
            if total_dist < distance[next_node]:
                distance[next_node] = total_dist
                heapq.heappush(queue, [total_dist, next_node])
    return distance

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])
    answer = dijkstra(graph, 1, N+1)

    cnt = 0
    for a in answer.values():
        if a<=K: cnt+=1
    return cnt