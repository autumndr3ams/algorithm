from copy import deepcopy

n, m = map(int, input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

d1 = [[(1,0)],[(-1,0)],[(0,1)],[(0,-1)]]
d2 = [[(1,0),(-1,0)],[(0,1),(0,-1)]]
d3 = [[(1,0),(0,1)],[(1,0),(0,-1)],[(-1,0),(0,1)],[(-1,0),(0,-1)]]
d4 = [[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)],[(0,-1),(-1,0),(0,1)]]
d5 = [[(1,0),(-1,0),(0,1),(0,-1)]]
dir_list = [d1,d2,d3,d4,d5]

min_result = 64 #최대 사각지대 수
cctv=[]
for i in range(n):
    for j in range(m):
        if 0<matrix[i][j]<6:
            cctv.append((i, j, matrix[i][j])  #i, j, 방향성 저장

def dfs(matrix, idx):
    global min_result
    if idx == len(cctv):
        value = 0
        for i in range(len(matrix)):
            value += matrix[i].count(0)
        min_result = min(min_result, value)
        return

    x, y, dn = cctv[idx]
    for direct in dir_list[dn-1]:
        newM = deepcopy(matrix)
        for d in direct:
            nx = x + d[0]
            ny = y + d[1]
            while 0<=nx<n and 0<=ny<m and newM[nx][ny]!=6:
                if newM[nx][ny] == 0:
                    newM[nx][ny] = '#'
                nx = nx + d[0]
                ny = ny + d[1]
        dfs(newM, idx+1)
                
dfs(matrix, 0)
print(min_result)
