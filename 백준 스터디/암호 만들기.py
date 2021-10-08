import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().split())
data = list(map(str, sys.stdin.readline().split()))
data.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
combi = list(combinations(data, l))
for com in combi:
  vcnt = 0
  ccnt = 0
  for s in com: 
    if s in vowels:
      vcnt+=1
    else:
      ccnt+=1
  if vcnt > 0 and ccnt > 1 :
    print("".join(com))