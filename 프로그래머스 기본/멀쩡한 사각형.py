def gcd(w,h):
    if w>=h:
        while h:
            w, h = h, w%h
        return w
    else:
        while w:
            w, h = h%w, w
        return h

def solution(w,h):
    total = w*h
    answer = total-(w+h-gcd(w,h))
    return answer