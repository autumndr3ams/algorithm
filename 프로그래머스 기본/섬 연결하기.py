def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2]) #cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) #섬이 중복되지 않도록 집합 사용
    
    while len(routes)!=n:
        for cost in costs:
            if cost[0] in routes and cost[1] in routes:
                #섬 두개가 모두 route 안에 있다면 패스
                continue
            if cost[0] in routes or cost[1] in routes:
                #아니라면 두 섬을 route에 넣고 cost를 더해줌, 중복은 set에서 알아서 삭제함
                routes.update([cost[0], cost[1]]) 
                answer+=cost[2]
                break

    return answer