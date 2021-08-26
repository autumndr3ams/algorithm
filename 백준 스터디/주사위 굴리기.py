"""
     동쪽       서쪽      북쪽      남쪽 
    1 -> 3     1 -> 4    1 -> 2    1 -> 5
    2 -> 2     2 -> 2    2 -> 6    2 -> 1
    3 -> 6     3 -> 1    3 -> 3    3 -> 3
    4 -> 1     4 -> 6    4 -> 4    4 -> 4
    5 -> 5     5 -> 5    5 -> 1    5 -> 6
    6 -> 4     6 -> 3    6 -> 5    6 -> 2
"""

import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#input
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(6)] #주사위

for i in range(k):
    dir = order[i]-1
    nx = x+dx[dir]
    ny = y+dy[dir]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if arr[nx][ny]==0:
        a[nx][ny] = dice[5]
    else:
        dice[5] = a[nx][ny]
        a[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
        
    
