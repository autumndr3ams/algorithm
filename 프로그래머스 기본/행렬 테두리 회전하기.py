def solution(rows, columns, queries):
    answer = []
    matrix = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i*columns+j+1
            
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        cur = matrix[x1][y1]
        minn = cur
        for k in range(x1, x2): #왼쪽 세로
            nex = matrix[k+1][y1] 
            matrix[k][y1] = nex
            minn = min(minn, nex)
        for k in range(y1, y2): #하단 가로
            nex = matrix[x2][k+1]
            matrix[x2][k] = nex
            minn = min(minn, nex)
        for k in range(x2, x1, -1): #우측 세로
            nex = matrix[k-1][y2]
            matrix[k][y2] = nex
            minn = min(minn, nex)
        for k in range(y2, y1, -1): #상단 가로
            nex = matrix[x1][k-1]
            matrix[x1][k] = nex
            minn = min(minn, nex)
        matrix[x1][y1+1] = cur
        answer.append(minn)
    return answer