def response(time_list, start, end):
    #초당 처리량을 구하는 함수
    cnt=0
    for time in time_list:
        if time[0] < end and time[1] > start:
            cnt+=1
    return cnt

def solution(lines):
    answer = 0
    time_list = []
    for line in lines:
        dateString = line[11:23]
        y, s, t = dateString.split(':')
        hh, mm, ss = s.split(':')
        t = t.replace('s','')
        
        end = float(hh)*3600 + float(mm)*60 + float(ss)
        start = end-float(t)+0.001
        
        time_list.append([start, end])
        
    for time in time_list:
        answer = max(answer, response(time_list, time[0], time[0]+1), response(time_list, time[1], time[1]+1))

    return answer
