from collections import deque
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cost_list = []

def bfs(board, visited, n):
    q = deque()
    q.append([0, 0, 0, 0]) #x, y, dir, cost
    visited[0][0] = 1
    while q:
        x, y , dir, c = q.popleft()
        
        if x==n-1 and y==n-1:
            cost_list.append(c)
            continue
        for i in range(n):
            nx = x+dx[i]
            ny = y+dy[i]
            nd = i
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                visited[nx][ny] = 1
                if dir==0: #first step
                    q.append([nx, ny, nd, 100])
                else:
                    if (dir%2==nd%2):
                        c += 100
                        q.append([nx, ny, nd, c])
                    else:
                        c += 600
                        q.append([nx, ny, nd, c])
                
                    
    
def solution(board):
    answer = 0
    n = len(board)
    answer_list = []
    visited = [[0 for _ in range(n)] for __ in range(n)]
    
    bfs(board, visited, n)
    answer = min(cost_list)
    
    return answer
