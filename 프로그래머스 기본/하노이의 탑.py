def hanoi(n, start, end, mid, answer):
    if n==1:
        answer.append([start, end])
        return
    hanoi(n-1, start, mid, end, answer)
    answer.append([start, end])
    hanoi(n-1, mid, end, start, answer)
    
    return answer
def solution(n):
    answer = []
    
    hanoi(n, 1, 3, 2, answer)
    return answer