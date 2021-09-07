def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1]) #나간 시점을 기준으로 정렬
    check = [False] * len(routes) #카메라를 만났는지 여부 저장

    for i in range(len(routes)):
        if check[i]:
            continue
        answer+=1
        camera = routes[i][1] #나간 시점에 카메라 설치
        for j in range(i, len(routes)):
            if routes[j][0]<=camera and camera<=routes[j][1]:
                check[j] = True
    return answer