import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
city = []
for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))
    
chickens = []
houses = []
chickenD = 0

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

for house in houses:
    d=[]
    for chicken in chickens:
        d.append(abs(chicken[0]-house[0])+abs(chicken[1]-house[1]))
    chickenD += min(d)

if m==len(chickens):
    print(chickenD)
else:
    candidates = list(combinations(chickens, m))
    tmpd_list=[]
    for candidate in candidates:
        tmpd=0
        for house in houses:
            d=[]
            for c in candidate:
                d.append(abs(c[0]-house[0])+abs(c[1]-house[1]))
            tmpd += min(d)
        tmpd_list.append(tmpd)
    print(min(tmpd_list))

        
