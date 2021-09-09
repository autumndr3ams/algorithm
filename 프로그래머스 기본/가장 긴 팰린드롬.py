def palindrome(check):
    if check != check[::-1]:
        return False
    return True

def solution(s):
    for cut in range(len(s), 1, -1):
        for start in range(len(s)-cut+1):
            check = s[start:start+cut]
            if palindrome(check):
                return cut
        
    return 1