import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # scovile을 힙화 시킴.

    # 스코빌 지수가 1개 남을 때까지 루프 실행
    while len(scoville) > 1:

        first = heapq.heappop(scoville)

        if first < K:
            break

        # 두번째로 작은 값 꺼내서 조합
        answer += 1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, (first + (second * 2)))



    # 모든 음식의 스코빌 지수가 K 이상인지 확인해야 하므로, 루프가 종류된 후에 검사 수행해야함.
    return answer if scoville[0] >= K else -1