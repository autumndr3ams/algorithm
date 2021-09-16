def solution(n, t, m, timetable):
    answer = ''
    crew = [int(time[:2])*60+int(time[3:]) for time in timetable]
    crew.sort()
    bus = [9*60+t*i for i in range(n)]

    total = 0 #이때까지 셔틀을 탄 사람, 다음 버스에 오를 크루의 인덱스
    for btime in bus:
        cnt=0 #한 버스에 탄 크루의 수
        while cnt<m and total<len(crew) and crew[total]<=btime:
            total+=1
            cnt+=1
        if cnt<m: answer = btime #버스에 자리가 남았을 때
        else: answer = crew[total-1]-1 #맨 마지막 크루보다 1분 먼저 도착
    answer = str(answer//60).zfill(2)+":"+str(answer%60).zfill(2)
    return answer