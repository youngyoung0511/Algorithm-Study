def solution(k, dungeons):
    def dfs(k, count): #모든 던전을 시도하며 최대 탐험 가능한 던전 수를 반환
        #k: 현재 피로도
        #count: 현재까지 탐험한 던전 수


        max_count = count  # 현재까지 탐험한 던전 수 저장

        for i in range(len(dungeons)): #던전 리스트의 인덱스 하나씩 순회해서
            #아직 방문하지 않은 던전만 탐험
            if not visited[i]:  # visited[i]는 해당 던전의 방문 여부를 나타내는 불리언 값
                #visited = [False, False, False]: 세 던전을 아직 탐험하지 않은 상태.
                #visited = [True, False, False]: 첫번째 던전 탐험

                #최소필요 피로도: minimum
                #소모 피로도: consumption
                #dungeons[i] = [80, 20]

                #최소필요 피로도랑 소모 피로도 가져와
                minimum, consumption = dungeons[i]

                #K가 최소 필요 피로도를 충족하면 방문.
                #하지만 조건을 충족하지 못하면 해당 던점 탐험 못해서 건너뜀
                if k >= minimum:  # 최소 필요 피로도를 만족하면 탐험 가능
                    visited[i] = True  # 방문 처리
                    #이 던전을 다시 탐험하지 않도록 visited[i]를 True로 설정
                    # 다음 탐험 진행
                    #피로도에서 소모 피로도 차감: k - consumption
                    #탐험 횟수 1증가: count+1
                    #최댓값 갱신: 현재 탐험 경로에서의 최대 탐험 횟수 저장
                    max_count = max(max_count, dfs(k - consumption, count + 1))
                    # 탐험 종료 후 원상복구
                    # 이 던던을 탐험하지 않은 상태로 되돌려야 다른 탐험 경로에서도 이 던전을 탐험할 수 있음.
                    visited[i] = False
                #그래서 모든 가능한 탐험 경로 중에서 최댓값 반환
        return max_count  # 최대 탐험 수 반환

    # 방문 여부 저장
    visited = [False] * len(dungeons)
    return dfs(k, 0)  # 초기 피로도와 탐험 횟수로 DFS 시작
