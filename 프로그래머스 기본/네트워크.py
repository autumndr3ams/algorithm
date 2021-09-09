from collections import deque

def bfs(n, computers, i, visited, q):

    while q:
        cur = q.popleft()
        visited[cur] = True
        for near in range(n):
            if near != cur and visited[near] == False and computers[cur][near] == 1:
                q.append(near)
        
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    q = deque()
    for i in range(n):
        if not visited[i]: 
            q.append(i)
            bfs(n, computers, i, visited, q)
            answer+=1
    return answer