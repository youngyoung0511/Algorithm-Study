
#전선을 끊을 때마다 DFS 또는 BFS로 두 네트워크 크기 확인

def solution(n,wires):

    #시작노드에서 연결된 모든 노드를 탐색하며 송천탑의 개수 반환
    def dfs(node, graph, visited):
        visited[node]=True #방문한 노드는 visited에 기록해서 다시 탐색하지 않도록 함
        count=1 #현재 노드

        for neighbor in graph[node]:
            if not visited[neighbor]:
                count+=dfs(neighbor,graph,visited)

        return count

    difference=0

    for i in range(len(wires)):
        #그래프 초기화
        graph=[[]for _ in range(n+1)]

        for j,(v1,v2) in enumerate(wires):
            if i==j: #전선 하나를 끊어
                continue
            #전선이 끊어진 상태에서 그래프 재구성
            graph[v1].append(v2)
            graph[v2].append(v1)

        #하나의 네트워크 크기 계산
        visited=[False]*(n+1)

        #count1: 첫번째 네트워크 크기: DFS로 탐색한 노드수
        #count2: 두번째 네트워크 크기: 전체 송전탑 수 n에서 count1을 뺀 값
        count_1=dfs(1,graph,visited)#첫번째 네트워크 크기
        count_2=n-count_1#다른 네트워크 크기

        difference=min(difference,abs(count_2-count_1))

    return difference