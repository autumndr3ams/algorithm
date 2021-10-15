from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    
    while q:
        cur_sum, idx = q.popleft()
        if idx == len(numbers):
            if cur_sum == target:
                answer+=1
        else:
            number = numbers[idx]
            q.append((cur_sum+number, idx+1))
            q.append((cur_sum-number, idx+1))
            
    return answer