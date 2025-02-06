
#1. N-1개를 경유지 두번째 판으로 옮겨놓음
#2. 가장 큰걸 목적지에 옮겨놓음
#3. N-1개를 두번째에서 목적지로 다시 옮겨놓음

#즉 N개의 원판을 k번째 장대로 옮기려면 목표 장대 빼고 나머지를 다른 장대에 몰아서 쌓아야함.

def hanoi(N,a,b,c): #N: 원판 개수, a: 초기 원판위치,b: 중간 경유지, c: 목적지

    # 재귀가 종료될 수 있도록 조건문 걸어놓음
    if N==1: #원판이 1개면 바로 목표 장대로 이동
        print(a,c)

    else: #원판이 2개 이상이면
        # 맨마지막 제외한걸 중간 경유지에 옮기고 맨마지막으로 목표점으로 옮김.
        # 그 후 나머지를 경유지에서 목표점으로 옮김

        #1. N-1개를 시작 a에서 목적지 b로 옮김
        hanoi(N-1,a,c,b)
        #2. 가장 큰 걸 목적지 c로 옮김. 가장 큰 원판만 이동시키는거라 print(a,c)로 이동 출력 음?
        print(a,c)
        #3. N-1개를 경유지 b에서 c로 옮김
        hanoi(N-1,b,a,c)

x=int(input())

print(2**x-1) #최소 이동 횟수(2^N-1)

#원판이 20개 이하일 때
if x<=20:
    hanoi(x,1,2,3)

