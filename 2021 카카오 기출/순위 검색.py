from itertools import combinations

def make_all_cases(temp):
    cases=[]
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case=''
            for idx in range(4):
                if idx not in li:
                    case+=temp[idx]
                else:
                    case+='-'
            cases.append(case)
    return cases
                    
def solution(info, query):
    answer = []
    case_score={}
    for i in info:
        i = i.split()
        key = i[:-1]
        value = int(i[-1])
        cases = make_all_cases(key) #16가지 경우의 수 만들기
        
        #case별로 점수 분류하기
        for case in cases:
            if case not in case_score.keys(): 
                case_score[case] = [value]
            else:
                case_score[case].append(value)
                
    #이진탐색을 위해 정렬            
    for key in case_score.keys():
        case_score[key].sort()
        
    for q in query:
        q = q.split()
        q_key = q[0]+q[2]+q[4]+q[6]
        q_value = int(q[-1])
        
        if q_key in case_score.keys():
            scoreList = case_score[q_key]
            if len(scoreList)>0:
                left, right=0, len(scoreList)
                while left<right:
                    mid = (left+right)//2
                    if scoreList[mid]>=q_value:
                        right = mid
                    else:
                        left = mid+1
                answer.append(len(scoreList)-left)
                
        else:
            answer.append(0)


        
    return answer
