def solution(word):

    vol=['A','E','I','O','U'] # 사용 가능한 글자
    weight=[781,156,31,6,1] # 각 자리의 가중치 설정

    position=0 #단어의 위치

    for i, char in enumerate(word):
        index=vol.index(char) #해당 글자의 인덱스. A=0, E=1
        position+=index*weight[i]+1 #자리 가중치 곱 + 1


    return position