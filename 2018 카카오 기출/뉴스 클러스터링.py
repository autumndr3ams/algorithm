def solution(str1, str2):
    list1 = []
    list2 = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            list1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            list2.append(str2[i:i+2].lower())
    
    if len(list1)>len(list2):
        inter = [list1.pop(list1.index(x)) for x in list2 if x in list1]
    else:
        inter = [list2.pop(list2.index(x)) for x in list1 if x in list2]
    
    uni = list1+list2
    
    if len(uni) == 0:
        return 65536

    answer = int(len(inter)/len(uni)*65536)
    return answer