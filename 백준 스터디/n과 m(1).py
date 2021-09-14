import sys
n, m = map(int, sys.stdin.readline().split())
visited = [False for _ in range(n)]
tmp = []

def backtracking(n, m, length):
    if m==length: 
        print(' '.join(map(str, tmp)))
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp.append(i+1)
            backtracking(n, m, length+1)
            visited[i] = False
            tmp.pop()

backtracking(n, m, 0)