
from collections import deque
def move(cur1, cur2, new_board):
    pos=[]
    #평행이동
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    y, x = 0, 1
    for dx, dy in direction:
        nxt1 = (cur1[y]+dy, cur1[x]+dx)
        nxt2 = (cur2[y]+dy, cur2[x]+dx)
        if new_board[nxt1[y]][nxt1[x]] == 0 and new_board[nxt2[y]][nxt2[x]] == 0:
            pos.append((nxt1, nxt2))
    #회전
    #가로방향
    if cur1[y] == cur2[y]:
        up, down = -1, 1
        for d in [up, down]:
            if new_board[cur1[y]+d][cur1[x]] == 0 and new_board[cur2[y]+d][cur2[x]] == 0:
                pos.append((cur1, (cur1[y]+d, cur1[x])))
                pos.append((cur2, (cur2[y]+d, cur2[x])))
    #세로방향
    else:
        left, right = -1, 1
        for d in [left, right]:
            if new_board[cur1[y]][cur1[x]+d] == 0 and new_board[cur2[y]][cur2[x]+d] == 0:
                pos.append(((cur1[y], cur1[x]+d), cur1))
                pos.append(((cur2[y], cur2[x]+d), cur2))
                
    return pos

def solution(board):
    answer = 0
    n = len(board)
    #board 외벽 감싸주기
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    q = deque([((1, 1), (1, 2), 0)])
    visited = set([((1,1), (1,2))]) #시간 절약 위해
    while q:
        cur1, cur2, cnt = q.popleft()
        if cur1 == (n,n) or cur2 == (n,n):
            return cnt
        for p in move(cur1, cur2, new_board):
            if p not in visited:
                q.append((*p, cnt+1))
                visited.add(p)
   