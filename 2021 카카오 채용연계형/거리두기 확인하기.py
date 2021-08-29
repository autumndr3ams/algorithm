from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(place, person):
    q = deque([person])
    visited = [[False]*5 for _ in range(5)]
    
    while q:
        x, y, d = q.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            nd = d+1
            
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if place[nx][ny] == 'P':
                    #다음 좌표가 P인데 아직 2 이하로 움직였다면(2 이하의 거리에 사람이 있다면)
                    if nd<=2:
                        return False
                elif place[nx][ny] == 'O':
                    if nd == 1:
                        q.append([nx, ny, nd])
    return True
            
def solution(places):
    answer = []
    n = len(places)
    
    for place in places:
        flag = 1
        for i in range(n):
            for j in range(n):
                if place[i][j] == 'P':
                    result = bfs(place, [i, j, 0]) #좌표와 이동count
                    if not result: 
                        flag = 0
        answer.append(flag)  
    return answer