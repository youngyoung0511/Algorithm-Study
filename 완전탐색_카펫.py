
def solution(brown, yellow):
    #전체 격자 수
    total=brown+yellow

    #전체 격자 수의 약수 쌍 구하기
    for height in range(1,int(total**0.5)+1):
        if total % height==0:
            width=total//height #너비 계산

            #갈색 격자 수가 조건에 맞는지 확인
            if 2 *(width+height-2)==brown: #테두리 격자가 갈색격자와 동일한지 확인
                return [width,height] #조건에 맞는 (가로, 세로) 반환