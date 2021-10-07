import math
def solution(n, stations, w):
    answer = 0
    apart=[]
    for i in range(1, len(stations)):
        apart.append((stations[i]-w)-(stations[i-1]+w)-1)
    apart.append(stations[0]-w-1)
    apart.append(n-(stations[-1]+w))

    for a in apart:
        if a<=0: continue
        answer+=math.ceil(a/(2*w+1))
    return answer