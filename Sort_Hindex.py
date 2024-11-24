def solution(citations):

    # 빈 리스트 처리
    if not citations: #논문이 하나도 없는 경우 처리. 비어있으면 H-index는 0
        return 0

    #1. 내림차순으로 정렬
    citations.sort(reverse=True)

    #2. index와 논문 인용 수 비교.
    #i: 각 논문의 인덱스, citation: 인용횟수
    #각 논문의 인덱스 i와 인용횟수 citation을 가져옴
    for i, citation in enumerate(citations):
        # citations=[6,5,3,1,0]
        #i=0, citation=6
        #i=1, citation=5
        #i=2, citation=3....


        #3. 인용수가 index+1보다 작거나 같으면 해당 index 반환
        # i=0, citation=6 (6>1이므로 불만족)
        # i=1, citation=5 (5>2 조건 불만족)
        # i=2, citation=3 (3>2 조건 만족)
        if citation<=i:
            return i

    # 모든 논문이 조건을 만족하면 논문 수 반환
    return len(citations)