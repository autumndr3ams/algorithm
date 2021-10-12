def solution(n, s):
    answer = []
    if n>s: return [-1]
    
    for i in range(n):
        answer.append((s//n))
    x = s%n
    i=-1
    while x>0:
        answer[i]+=1
        x-=1
        i-=1
    return answer