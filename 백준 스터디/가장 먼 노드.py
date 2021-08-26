from collections import deque

def bfs(v, visited, graph):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        cur = q.popleft()
        n = cur[0]
        cnt = cur[1]
        if visited[n] == -1:  #아직 방문하지 않았다면
            visited[n] = cnt
            for next in graph[n]:
                q.append([next, cnt+1])
        
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited = [-1 for _ in range(n+1)]  #방문여부 체크 
    bfs(1, visited, graph)
    
    for v in visited:
        if v == max(visited):
            answer+=1
    return answer
