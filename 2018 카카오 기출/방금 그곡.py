def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music

def solution(m, musicinfos):
    answer=[]
    m = change(m)
    idx=0
    for info in musicinfos:
        idx+=1
        start, end, music, code = info.split(',')
        start = int(start[:2])*60+int(start[3:])
        end = int(end[:2])*60+int(end[3:])
        time = end - start
        
        code = change(code)
        x = time//len(code)
        y = time%len(code)
        
        fullcode = code*x + code[:y]
        
        if m in fullcode:
            answer.append([time, idx, music])
            
    if not answer:
        return '(None)'
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x:(-x[0], x[1]))
        return answer[0][2]