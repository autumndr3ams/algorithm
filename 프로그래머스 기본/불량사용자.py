from itertools import permutations
def check(case, banned_id):
    for i in range(len(banned_id)):
        if len(case[i]) != len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != case[i][j]:
                return False
    return True
            
def solution(user_id, banned_id):
    answer = 0
    cases = list(permutations(user_id, len(banned_id)))
    banned_list = []
    for case in cases:
        if not check(case, banned_id):
            continue
        else:
            case = set(case)
            if case not in banned_list:
                banned_list.append(case)
    answer = len(banned_list)
    return answer