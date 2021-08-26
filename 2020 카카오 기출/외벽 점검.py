from itertools import permutations

def solution(n, weak, dist):
    answer = []
    L = len(weak)
    # 시계/반시계 문제 해결하기
    # 4에서 반시계방향 = 9에서 시계방향이므로 배열을 2배 늘려 해결
    weak_point = weak + [w+n for w in weak]
    candidates = list(permutations(dist))

    for i, start in enumerate(weak):
        print(i)
        for friends in candidates:
            print(friends)
            cnt = 1           
            position = start #시작점 잡기
            #친구 배치
            for friend in friends:
                position += friend
                if position < weak_point[i+L-1]:
                    cnt+=1 #친구 추가
                    #현재 위치보다 더 멀리 있는 취약지점 중 가장 가까운 곳
                    position = [w for w in weak_point[i+1:i+L] if w > position][0]
                else:
                    answer.append(cnt)
                    break
                    
            
    return min(answer) if answer else -1