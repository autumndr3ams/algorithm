def check(ans):
    for x, y, what in ans:
        # 기둥
        # 1. 바닥위에 있거나
        # 2. 보의 한쪽 끝 부분에 있거나
        # 3. 다른 기둥 위에 있어야함
        if what == 0 :
            if y==0 or (x-1, y, 1) in ans or (x, y, 1) in ans or (x, y-1, 0) in ans:
                continue
            else:
                return False
        # 보
        # 1. 한쪽 끝 부분이 기둥위에 있거나
        # 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야함
        else:
            if (x, y-1, 0) in ans or (x+1, y-1, 0) in ans or ((x-1, y, 1) in ans and (x+1, y, 1) in ans):
                continue
            else: 
                return False
        return True
    
def solution(n, build_frame):
    answer = set()
    
    for build in build_frame:
        x, y, what, how = build
        if how == 1:
            answer.add((x, y, what))
            if check(answer) == False:
                answer.remove((x, y, what))
        else:
            answer.remove((x, y, what))
            if check(answer) == False:
                answer.add((x, y, what))          
    answer = [list(i) for i in answer]
    answer = sorted(answer, key = lambda x: (x[0], x[1], x[2]))            
    return answer
