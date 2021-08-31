def solution(n, k, cmd):
    exist = [True for _ in range(n)]
    up = [-1] + [x for x in range(n-1)]
    down = [x for x in range(1, n)]+[-1]
    deleted = []
    
    for c in cmd:
        op = c[0]
        if op == 'U':
            val = int(c.split()[1])
            for _ in range(val):
                k = up[k]
        elif op=='D':
            val = int(c.split()[1])
            for _ in range(val):
                k = down[k]
        elif op=='C':
            if up[k] != -1: #현재 위치가 맨 위가 아님
                down[up[k]] = down[k]
            if down[k] != -1: #현재 위치가 맨 아래가 아님
                up[down[k]] = up[k]
            exist[k] = False
            deleted.append(k)
            k = down[k] if down[k] != -1 else up[k]
        elif op=="Z":
            d = deleted.pop()
            if up[d] != -1:
                down[up[d]] = d
            if down[d] != -1:
                up[down[d]] = d
            exist[d] = True
    return ''.join(['O' if x else 'X' for x in exist])
            