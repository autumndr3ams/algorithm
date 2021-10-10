import queue
from collections import deque
def solution(n, queries):
  answer=[]
  new = [deque() for _ in range(n)]
  front = queries[0][0]
  for q in queries:
    idx, value = q
    if idx>=0:
      new[idx].append(value)
    else:
      answer.append(new[front].popleft())
      front = (front+1)%n
     
  return answer

n = 4
queries=[[0,1], [0,2], [0,3], [1,4], [1,5], [2,6], [3,7], [-1,-1]]
print(solution(n, queries))


