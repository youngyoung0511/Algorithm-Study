def solution(number, k):
    result = ""
    start = 0

    #탐색 범위 설정
    #만들 숫자의 자릿수는 len(number) - k이므로, 탐색은 숫자의 전체 길이에서 k를 뺀 범위까지 진행
    end = len(number) - k

    # 최대 숫자 찾기 반복
    for _ in range(len(number) - k):
        max_digit = '0'

        # 현재 범위 내에서 가장 큰 숫자를 찾는다
        #number의 start부터 k+1까지의 범위에서 가장 큰 숫자를 찾습니다.
        for i in range(start, k + 1):
            if number[i] > max_digit: #현재 숫자가 최대 숫자보다 크다면 max_digit을 업데이트
                max_digit = number[i]
                start = i + 1 #다음 탐색 범위를 i+1로 설정.
                if max_digit == '9':  # 최대 숫자인 '9'를 만나면 더 이상 탐색할 필요가 없으므로 반복 종료.
                    break
        result += max_digit #선택한 최대 숫자를 result에 추가
        k -= start #선택한 최대 숫자까지의 탐색 과정에서 제거된 숫자의 개수를 반영

    return result
