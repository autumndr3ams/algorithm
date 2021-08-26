def solution(s):
    answer = 0
    result=[]
    if len(s)==1: return 1
    for i in range(1, (len(s)//2)+1):
        cnt = 1
        res = ''
        curStr = s[:i]
        for j in range(i, len(s), i):
            print(curStr)
            if curStr == s[j:j+i]:
                cnt+=1
            else:
                if cnt==1:
                    res+=curStr
                else:
                    res = res+str(cnt)+curStr
                curStr = s[j:j+i]
                cnt = 1 
        result.append(len(res))
    answer = min(result)
    return answer
