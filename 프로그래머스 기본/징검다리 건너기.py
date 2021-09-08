def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left<=right:
        #temp = stones.copy()
        mid = (left+right)//2
        cnt = 0
        for s in stones:
            if (s-mid)<=0:
                cnt+=1
            else:
                cnt = 0
            if cnt>=k:
                break
        if cnt>=k:
            right = mid-1
        else:
            left = mid+1
            
    return left