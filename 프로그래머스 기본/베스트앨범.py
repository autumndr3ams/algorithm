from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(int);  #총 재생횟수
    play_dic = defaultdict(lambda:[]) #(고유번호, 재생횟수)
    
    i=0
    for g, p in zip(genres, plays):
        genre_dic[g] += p
        play_dic[g].append((i, p))
        i+=1
    
    genre_dic = sorted(genre_dic.items(), key = lambda x:x[1], reverse = True)
    
    for g in genre_dic:
        sorted_play = sorted(play_dic[g[0]], key = lambda x:x[1], reverse = True)
        answer.append(sorted_play[0][0])
        if len(sorted_play) > 1:
            answer.append(sorted_play[1][0])
    return answer