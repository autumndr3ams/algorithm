def rotate(key):
    n = len(key)
    tmp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = key[i][j]
    return tmp

def check(key, lock, mapSize, x, y, start, end):
    expendMap = [[0]*mapSize for _ in range(mapSize)]
    
    #map에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendMap[x+i][y+j]+=key[i][j]
            
    for i in range(start, end):
        for j in range(start, end):
            expendMap[i][j]+=lock[i-start][j-start]
            if expendMap[i][j]!=1:
                return False
    return True

def solution(key, lock):
    answer = True
    mapSize = (len(key)-1)*2 + len(lock)
    start = len(key)-1 #map에서 lock 배열이 시작하는 위치
    end = start + len(lock) #map에서 lock 배열이 끝나는 위치
    
    for d in range(4):
        #lock은 고정, key만 움직임
        for i in range(end):
            for j in range(end):
                if check(key, lock, mapSize, i, j, start, end):
                    return True
        key = rotate(key)

    return False
