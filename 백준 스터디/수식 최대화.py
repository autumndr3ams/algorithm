import itertools

def calc(x, y, op):
    if op=="*":
        return x*y
    if op=="+":
        return x+y
    else: return x-y
    


def solution(expression):
    answer = 0
    numbers, operations=[],[]
    tmp=''
    #숫자, 연산자 분리
    for i in range(len(expression)):
        #숫자라면
        if expression[i].isdigit():
            tmp+=expression[i]
        #연산자라면
        else:
            numbers.append(int(tmp))
            tmp=''
            operations.append(expression[i])
    numbers.append(int(tmp))
        
    priority=['+', '-', '*']
    priority=list(itertools.permutations(priority,3))
    
    for order in priority:
        tmpOp=operations.copy()
        tmpN=numbers.copy()
        
        for i in range(len(order)):
            idx=0
            while idx<len(tmpOp):
                if tmpOp[idx]==order[i]:
                    tmpN[idx]=calc(tmpN[idx], tmpN[idx+1], order[i])
                    tmpOp.pop(idx)
                    tmpN.pop(idx+1)
                else:
                    idx+=1
        answer=max(answer, abs(tmpN[0]))
    
    return answer
