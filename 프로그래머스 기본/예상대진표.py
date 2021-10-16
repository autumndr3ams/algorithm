def solution(n,a,b):
    answer = 0

    while True:
        a = (a+1)//2
        b = (b+1)//2
        answer+=1
        if a==b:
            break

    return answer