def solution(record):
    answer = []
    dic={}
    
    for r in record:
        log = r.split()
        if log[0] == "Enter" or log[0] == "Change":
            dic[log[1]] = log[2]
    
    for r in record:
        log = r.split()
        if log[0] == "Enter":
            answer.append(dic[log[1]]+"님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(dic[log[1]]+"님이 나갔습니다.")

    return answer