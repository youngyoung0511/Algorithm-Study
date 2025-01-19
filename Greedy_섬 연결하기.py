
#MST(최소 스패닝 트리)란?
#스패닝 트리(Spanning Tree)는 그래프의 모든 노드를 연결하면서 사이클(순환)이 없는 트리 구조입니다.
#섬 0 --- 섬 1
# |         |
#섬 2 --- 섬 3
#섬을 연결하는 다리를 선택하되, 비용을 최소화

# MST를 구하는 대표적인 알고리즘:
# 크루스칼 알고리즘: 비용이 작은 간선(다리)부터 하나씩 선택하여 MST를 만듭니다.
# 이때, 사이클을 확인하기 위해 유니온-파인드를 사용

# 유니온-파인드의 역할
# 유니온-파인드는 서로 연결된 노드들이 같은 집합에 속하는지를 빠르게 판별하기 위한 자료구조입니다.
# 크루스칼 알고리즘에서 사이클을 방지하기 위해 사용됩니다.
# 즉, 다리를 추가하기 전에 두 섬이 이미 같은 집합에 속해 있다면,
# 사이클이 발생하므로 다리를 추가하지 않습니다.

# 유니온-파인드의 동작 원리

# find(x):
# 노드 x가 속한 집합의 대표 노드(루트)를 찾습니다.
# 경로 압축(Path Compression)을 통해 효율적으로 작동합니다.

# union(x, y):
# 노드 x와 y가 속한 두 집합을 하나로 합칩니다.
# 트리의 높이를 최소화하기 위해 **랭크(rank)**를 사용합니다.


def solution(n, costs):
    #1. 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2]) # 비용을 오름차순으로 정렬
    # costs 리스트는 [섬1, 섬2, 비용] 형태로 구성
    # 비용이 낮은 다리부터 처리하기 위해 비용 기준으로 정렬

    #2. 유니온 - 파인드 초기화
    parent = [i for i in range(n)] # 각 섬은 자기 자신을 부모로 초기화
    rank = [0]*n # 각 섬의 랭크(트리 높이)를 0으로 초기화

    # 유니온 - 파인드 함수 정의

    # find(): 특정 섬이 속한 최상위 부모를 찾음.
    def find(parent, x):
        if parent[x] != x:# 현재 노드 x가 자기 자신이 아니라면 (즉, 루트 노드가 아니라면)
            parent[x] = find(parent, parent[x]) # x의 부모를 재귀적으로 찾아 경로 압축
        return parent[x] # x가 속한 최상위 부모(루트)를 반환

    #parent = [0, 0, 0, 3]  # 1과 2의 부모가 0임
    #find(parent, 2) 호출 시:
    #parent[2] != 2이므로 find(parent, 0) 호출.
    #경로 압축: parent[2] = 0.
    #반환값: 0.


    # union(): 두 섬을 같은 집합으로 합침.
    def union(parent, rank, x, y): #x와 y가 속한 집합을 하나로 합치는 함수
        root_x = find(parent, x)# x의 루트 노드를 찾음
        root_y = find(parent, y)# y의 루트 노드를 찾음
        if root_x != root_y:# 두 노드가 서로 다른 집합에 속한 경우에만 합침
            if rank[root_x] > rank[root_y]:# root_x의 트리 높이가 더 크다면
                parent[root_y] = root_x# root_y를 root_x 아래에 붙임
            elif rank[root_x] < rank[root_y]:# root_y의 트리 높이가 더 크다면
                parent[root_x] = root_y # root_x를 root_y 아래에 붙임
            else:# 두 트리의 높이가 같다면
                parent[root_y] = root_x # root_y를 root_x 아래에 붙임
                rank[root_x] += 1  # root_x의 트리 높이를 1 증가


    # 초기 상태:
    # parent = [0, 1, 2, 3]
    # rank = [0, 0, 0, 0]

    # union(0, 1) 호출:
    # find(parent, 0) → 0.
    # find(parent, 1) → 1.
    # rank[0] == rank[1] → 두 트리의 높이가 같으므로:

    # parent = [0, 0, 2, 3]
    # rank = [1, 0, 0, 0]


    # union(1, 2) 호출:
    # find(parent, 1) → 0 (경로 압축으로 1의 부모는 0임).
    # find(parent, 2) → 2.
    # rank[0] > rank[2] → 트리 2를 트리 0 아래에 붙임:

    # parent = [0, 0, 0, 3]
    # rank = [1, 0, 0, 0]

    #3. (MST) 최소 스패닝 트리 구성: 정렬된 cost를 순회하며 수행
    total=0 # MST의 총 비용을 저장하는 변수
    for u,v,cost in costs:# 정렬된 costs 리스트를 순회
        if find(parent, u)!=find(parent,v): # u와 v가 같은 집합에 속하지 않으면
            # 두 섬이 연결되어 있지 않으면 두 섬을 같은 집합으로 합침
            union(parent,rank,u,v) # 두 섬 u와 v를 같은 집합으로 연결
            total +=cost  # u와 v를 연결한 비용을 total에 추가

    # 모든 섬이 연결되었을 때 총 비용 반환
    return total

