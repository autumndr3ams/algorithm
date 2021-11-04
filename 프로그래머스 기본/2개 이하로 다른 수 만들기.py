def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0:
            answer.append(number+1) #짝수라면 맨 끝에 0을 1로 바꾸면 정답
        else:
            binary = '0'+bin(number)[2:] #출력결과가 0b~
            idx = binary.rfind('0')
            binary = list(binary)
            binary[idx] = '1'
            binary[idx+1] = '0'
            answer.append(int(''.join(binary),2))
    return answer