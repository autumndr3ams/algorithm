from itertools import combinations

def uniqueness(relation, c):
    check = set()
    
    for r in relation:
        data=[]
        for i in c:
            data.append(r[i])
        check.add(tuple(data)) #set의 원소는 immutable해야함
    if len(check) == len(relation):
        return True
    else:
        return False
    
def minimality(candi, candidates):
    for x in candidates:
        if x<candi:
            return False
    return True
    
def solution(relation):
    answer = 0
    
    if len(relation)>0:
        colSize = len(relation[0])
        n = [i for i in range(colSize)]
    #가능한 모든 조합
        combi = []
        for i in range(1, colSize+1):
            combi.extend(map(set, combinations(n,i)))
    
        candidates=[] #유일성 만족하는 조합 리스트
        for c in combi:
            if uniqueness(relation, c):
                candidates.append(c)
            
        for candi in candidates:
            if minimality(candi, candidates):
                answer+=1

    return answer