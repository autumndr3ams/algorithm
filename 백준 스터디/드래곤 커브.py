import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
matrix = [[0]*101 for _ in ragne(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    matrix[x][y] = 1
    move = [d] #방향
    for _ in range(g):
        tmp = [] #이전단계 방향 기억
        for i in range(len(move)):
            tmp.append((move[-i-1]+1)%4)
        move.extend(tmp)

    for i in move:
        nx = x+dy[i]
        ny = y+dy[i]
        matrix[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j i n range(100):
        if matrix[i][j]:
            if matrix[i+1][j] and matrix[i][j+1] and matrix[i+1][j+1]:
                ans+=1

print(ans)
