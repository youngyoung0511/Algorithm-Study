def solution(n, lost, reserve):

# set 연산을 사용하여 두 리스트 간 교집합을 제거
#(스스로 해결 가능한 사람 제거)


# 여벌 체육복을 가져왔으나 자신의 체육복이 도난당한 학생은 스스로 해결 가능하므로
# 도난당한 리스트(lost)와 여벌 리스트(reserve)에 포함되지 않게 처리

# a_lost: 체육복을 도난당한 학생 중 여벌 체육복이 없는 학생
# a_reserve: 여벌 체육복을 가진 학생 중 체육복을 도난당하지 않은 학생
    a_lost=list(set(lost)-set(reserve))
    a_reserve=list(set(reserve)-set(lost))

#번호 순으로 처리하기 위해 actual_lost와 actual_reserve를 정렬
    #정렬하고 순차적 처리
    a_reserve.sort()
    a_lost.sort()

    #빌려줄 수 있는 학생
    for r in a_reserve:
        #여벌 체육복을 가진 학생(actual_reserve)을 순회
        #앞번호(r - 1) 또는 뒷번호(r + 1)의 학생이 체육복이 없는 경우 빌려줍
        if r-1 in a_lost: #앞번호의 학생이 체육복이 없으면, 그 학생을 a_lost에서 제거(체육복을 빌린 것으로 처리
            a_lost.remove(r-1) #체육복을 빌려준 학생은 actual_lost 리스트에서 제거
        elif r+1 in a_lost: #r+1 in a_lost: 앞번호가 없고, 뒷번호의 학생이 체육복이 없으면, 그 학생을 a_lost에서 제거.
            a_lost.remove(r+1)

    # 총 학생 수 n에서 체육복을 빌리지 못한 학생 수(len(a_lost))를 뺀 값을 반환.
    return n-len(a_lost)