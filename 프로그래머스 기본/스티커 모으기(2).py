def solution(sticker):
    answer = 0
    if (len(sticker)==1): return sticker[0]
    elif (len(sticker)==2): return max(sticker[0], sticker[1])
    
    #0번째를 뜯었을 때
    dp=[0]*len(sticker)
    dp[0] = sticker[0]
    dp[1] = sticker[0] #0번째를 뜯으면 1번째는 뜯지 못함
    for i in range(2, len(sticker)-1): #마지막도 뜯지 못함
        dp[i] = max(dp[i-2]+sticker[i], dp[i-1])
    answer = dp[len(sticker)-2]
    
    #1번째를 뜯었을 때
    dp=[0]*len(sticker)
    dp[0], dp[1] = 0, sticker[1]
    for i in range(2, len(sticker)): #마지막도 뜯지 못함
        dp[i] = max(dp[i-2]+sticker[i], dp[i-1])
    answer = max(answer, dp[len(sticker)-1])

    return answer