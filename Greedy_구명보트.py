def solution(people, limit):
    # 몸무게를 오름차순으로 정렬
    #가장 가벼운 사람은 리스트의 앞쪽(people[0]), 가장 무거운 사람은 리스트의 뒤쪽(people[-1])에 위치
    people.sort()
    boats = 0

    while people:
        #  구명보트는 무게 제한이 있으므로, 가장 무거운 사람부터 우선적으로 처리
        # 가장 무거운 사람을 pop. 가장 무거운 사람을 리스트에서 제거
        heaviest = people.pop()


        # 가장 가벼운 사람과 함께 태울 수 있는지 확인
        #people[0]: 남아 있는 사람들 중 가장 가벼운 사람.
        if people and people[0] + heaviest <= limit:
            #가장 무거운 사람과 가장 가벼운 사람의 합이 무게 제한을 초과하지 않을 경우, 두 사람을 한 보트에 태웁니다.
            people.pop(0)  # 가장 가벼운 사람을 pop
        # 보트를 하나 사용
        boats += 1

    return boats
