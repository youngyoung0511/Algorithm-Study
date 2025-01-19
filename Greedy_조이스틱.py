def solution(name):

    # 알파벳 이동 계산
    def move(char):
        return min(ord(char)-ord('A'),ord('Z')-ord(char)+1)

    # 예: char = 'J'
    # 1. ord('J') - ord('A')  # 74 - 65 = 9 / 9번 조작
    # 2. ord('Z') - ord('J') + 1  # 90 - 74 + 1 = 17 / 17번 조작
    # 중에 min 값 채택-> 특정 알파벳까지 이동하는데 필요한 최소 조작 횟수 계산

    # 전체 알파벳 이동 횟수 계산: name의 각 문자를 A에서 해당 문자로 변경하는데 필요한 총 알파벳 이동 횟수

    total=sum(move(char) for char in name)

    # 예: name = "JAZ"
    # move('J') = 9 / move('A') = 0 / move('Z') = 1
    # total: 10

    # <<커서>> 이동 최솟값 계산
    # 1. 그냥 오른쪽으로 쭉 이동
    # 2. 특정 위치에서 뒤로 돌아가기
    # 3. 연속된 A 구간 건너뛰기

    # 전체 문자열 길이랑 기본값 설정
    n=len(name) # 문자열 길이. 커서가 움직일 전체 범위

    # 1번 경우: 오른쪽으로만 끝까지 가는 경우의 이동 횟수
    right=n-1
    # 예: name = "JAZZ" → 커서를 3번 오른쪽으로 움직이면 끝.

    # 2번경우: 특정 위치에서 뒤로 돌아가기
    for i in range(n): #탐색 가능한 범위에서
        next_idx=i+1 #다음의 위치에서 연속된 A를 건너뛰고,A가 아닌 위치를 찾음

        #다음 A가 아닌 위치 찾기
        while next_idx < n and name[next_idx]=='A':
            # 예: name = "ABAAAC" → i = 1일 때, next_idx = 4 (A들을 건너뛰고 C를 찾음)
            next_idx+=1
        # 이동 거리 계산
        # 현재위치 i에서 A가 아닌 특정 위치로 가는 총 이동거리
        distance = i + min(i, n - next_idx) + (n - next_idx)
        # i: 현재 위치까지 이동한 거리.
        # min(i, n - next_idx): 뒤로 돌아가는 거리와 앞으로 가는 거리 중 더 짧은 거리
        # 뒤로 돌아가는 거리: 현재 위치에서 다시 시작점으로 돌아가야 하는 거리 (i).
        # 앞으로 가는 거리: 현재 위치를 기준으로 끝까지 가야 하는 거리 (n - next_idx).

        # 예: name = "JAAZ"
        # 원래 로직:
        # i = 1일 때, distance = 1 + 1 + (4 - 3) = 3.
        # 이 계산은 무조건 되돌아가는 거리(1 + 1)를 포함해 불필요한 이동을 추가.
        # 수정된 로직:
        # i = 1일 때, distance = 1 + min(1, 4 - 3) + (4 - 3) = 1 + 1 + 1 = 3.
        # 뒤로 돌아가는 거리와 앞으로 가는 거리 중 최소값을 선택하여 정확한 이동 거리 계산.

        # 최소 이동 거리 업데이트
        # right: 현재까지 계산된 커서 이동 거리의 최솟값
        # 새로운 경로 d
        right=min(right, distance)

        if name=="A"*n:
            return 0

    # 알파벳 이동 횟수 total와 커서 이동 횟수 right 합한 값
    return total+right


