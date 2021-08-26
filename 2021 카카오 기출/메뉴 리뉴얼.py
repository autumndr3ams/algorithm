from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = [] 
        for order in orders:
            combi = combinations(sorted(order),c)
            temp += combi
        cnt = Counter(temp)
        
        if len(cnt) != 0 and max(cnt.values()) != 1:
            for f in cnt:
                if cnt[f] == max(cnt.values()):
                    answer += [''.join(f)]
    
    return sorted(answer)
