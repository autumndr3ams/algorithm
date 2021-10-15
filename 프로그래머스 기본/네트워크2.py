from collections import deque

def bfs(n, computers, q, visited):
    while q:
        cur_node = q.popleft()
        visited[cur_node] = True
        for next_node in range(n):
            if next_node != cur_node and not visited[next_node] and computers[cur_node][next_node]:
                q.append(next_node)
        
        
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    q = deque()
    
    for i in range(n):
        if not visited[i]:
            q.append(i)
            bfs(n, computers, q, visited)
            answer+=1
    return answer