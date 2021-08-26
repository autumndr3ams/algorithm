import heapq
import sys

def dijkstra(graph, start):
    dist = {node: sys.maxsize for node in graph}
    dist[start] = 0 #시작 노드의 거리는 0으로 설정
    queue=[]
    #우선순위 큐에 시작노드 삽입
    #min heap이 첫 번째 데이터를 기준으로 정렬하기 때문에 거리-노드 순으로
    heapq.heappush(queue, [dist[start], start])
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        #이미 저장된 거리가 더 작다면 pass
        if dist[cur_node] < cur_dist: continue
        #현재 노드에서 인접한 노드 순회
        for adj_node, weight in graph[cur_node].items():
            distance = cur_dist + weight
            if distance < dist[adj_node]:
                #새로 계산한 거리가 더 작으면 변경
                dist[adj_node] = distance
                heapq.heappush(queue,[distance, adj_node])
                
    return dist

def solution(n, s, a, b, fares):
    answer = 0
    graph = {}
    
    for i in range(n):
        graph[i+1] = {}
    
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    #start에서 각 노드까지 최소 거리를 구함
    candidate = dijkstra(graph, s)
    
    answer = candidate[a]+candidate[b]
    
    for t in range(1, n+1):
        if t==s: continue
        temp = dijkstra(graph, t)
        answer = min(answer, candidate[t]+temp[a]+temp[b])
    
    return answer
