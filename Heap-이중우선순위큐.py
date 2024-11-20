import  heapq

def solution(operations):

    minheap=[] #최소힙
    maxheap=[] #최대힙
    #삽입된 값 중 유효한 값만 추적하기 위한 집합.
    #삭제된 값은 visited에서 제거
    visited=set() #유효한 요소를 추적하는 집합

    # 명령어 순회
    for operation in operations:
        command, value=operation.split()#명령어를 공백 기준으로 분리
        value=int(value)#명령어에 포함된 숫자를 문자열에서 int로 변환

        #삽입 명령어 I
        if command== 'I':
            # 해당 숫자 삽입
            heapq.heappush(minheap,value)#최소힙에 삽입 - 가장 작은 값이 루트
            heapq.heappush(maxheap, -value) #최대힙은 음수로 변환하여 삽입해서 최대힙처럼 동작하도록 함
            visited.add(value) # 삽입된 값을 visited 집합에 추가해 유효한 값으로 추적


        #삭제 명령어 D
        elif command=='D':


            #value가 1이면 최대힙에서 삭제
           if value==1:

               # 힙에 남아 있는 값이 유효한지 확인하고, 유효하지 않은 값 제거
               # maxheap에 없고 루트 값이(-maxheap[0])이 visited에 없으면 반복
               while maxheap and -maxheap[0] not in visited:
                   # 힙의 루트를 꺼내서 제거함.
                   heapq.heappop(maxheap)

               if maxheap: #maxheap에 유효한 값이 남아있다면 최대값 제거하고 visited에서도 제거
                   visited.remove(-heapq.heappop(maxheap))


           #value가 -1이면 최소힙에서 삭제
           elif value==-1:

               # minheap의 최소값이 visited에 없으면 이는 삭제된 값이라 제거함
               while minheap and minheap[0] not in visited:
                   heapq.heappop(minheap)
            #minheap에 유효한 값이 있으면 최솟값 제거하고, visited에도 제거
               if minheap:
                   visited.remove(heapq.heappop(minheap))



    # 힙 정리
    # 명령어 처리가 끝난 뒤에도 힙에서 유효하지 않은 값을 제거함.
    while maxheap and -maxheap[0] not in visited:
        heapq.heappop(maxheap)
    while minheap and minheap[0] not in visited:
        heapq.heappop(minheap)



    #결과 반환
    if not visited:
        return [0,0]
    else:
        #heapq는 최소힙 형태이기때문에 최대힙을 구현하려면 -를 붙인다
        return [-heapq.heappop(maxheap), heapq.heappop(minheap)]
