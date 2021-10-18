import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j]==0]

def is_promising(i, j):
  candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for k in range(9):
    if board[i][k] in candidates:
      candidates.remove(board[i][k])
    if board[k][j] in candidates:
      candidates.remove(board[k][j])
  
  i//=3
  j//=3
  for a in range(i*3, (i+1)*3):
    for b in range(j*3, (j+1)*3):
      if board[a][b] in candidates:
        candidates.remove(board[a][b])
  return candidates

flag = False
def dfs(x):
  global flag
  if flag: #이미 출력되었으면 ㅠㅐ스
    return

  if x==len(zeros):
    for row in board:
      print(*row)
    flag = True
    return
  else:
    (i, j) = zeros[x]
    candi = is_promising(i, j) #될만한 것들 뽑기
    for num in candi:
      board[i][j] = num
      dfs(x+1)
      board[i][j] = 0 #정답이 없을 때 초기화

dfs(0)