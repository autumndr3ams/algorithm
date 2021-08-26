def time_to_sec(time):
    h, m, s = time.split(":")
    res = int(h)*3600+int(m)*60+int(s)
    return res
def sec_to_time(time):
    h = time//3600
    h ='0'+str(h) if h<10 else str(h)
    time = time%3600
    m = time//60
    m ='0'+str(m) if m<10 else str(m)
    time = time%60
    s ='0'+str(time) if time<10 else str(time)
    return h+':'+m+':'+s

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    all_time = [0 for _ in range(play_time+1)] #all_time[i] = i 시각에 시청중인 사람의 수
    
    for log in logs:
        start, end = log.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        #시작과 끝에 시청자 표시
        all_time[start]+=1
        all_time[end]-=1
    
    #구간 별 사용자 누적
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i]+all_time[i-1]
    #전체 구간 사용자 누적(한 번 더 해주어야함)
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i]+all_time[i-1]
    
    most_view = all_time[adv_time-1]
    most_time = 0
    #(현재 i의 누적 시청자수)- (i-adv_time의 누적 시청자수)=(해당 구간의 시청자수)
    for i in range(adv_time, play_time):
        if most_view < all_time[i] - all_time[i-adv_time]:
            most_view = all_time[i] - all_time[i-adv_time]
            most_time = i-adv_time+1
    
    answer = sec_to_time(most_time)
    return answer
