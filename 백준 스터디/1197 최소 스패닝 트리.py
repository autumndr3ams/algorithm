import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
visited = [False]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
  u, v, w = map(int, input().split())
  graph[u].append([w, v])
  graph[v].append([w, u])

def prim(graph, start):
  visited[start] = True
  candidateq = graph[start]
  heapq.heapify(candidateq)
  totalw = 0

  while candidateq:
    weight, next_node = heapq.heappop(candidateq)
    if not visited[next_node]:
      visited[next_node] = True
      totalw+=weight
      
      for edge in graph[next_node]:
        if not visited[edge[1]]:
          heapq.heappush(candidateq, edge)
  return totalw

print(prim(graph, 1))