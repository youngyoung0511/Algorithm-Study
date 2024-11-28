def solution(answers):
    # 각 수포자의 찍는 패턴
    first_pattern = [1, 2, 3, 4, 5]
    second_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    third_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자의 점수 저장
    scores = [0, 0, 0]

    # 정답과 각 수포자의 패턴 비교
    for i, answer in enumerate(answers):
        if answer == first_pattern[i % len(first_pattern)]: #첫번째 사람 맞으면 +1
            scores[0] += 1
        if answer == second_pattern[i % len(second_pattern)]: #두번재 사람 맞으면 +1
            scores[1] += 1
        if answer == third_pattern[i % len(third_pattern)]: #세번째 사람 맞으면 +1
            scores[2] += 1

    # 가장 높은 점수 계산
    max_score = max(scores)

    # 점수가 가장 높은 수포자 찾기
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return result
