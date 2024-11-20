# 최대값 찾고 남은 정렬 부분의 남은 데이터 정렬하는 방식이 좋을거 같다.
# 그리고 1번의 loop로 가능


def solution(numbers):
    answer=' ' #처음에는 빈 문자열로 초기화
    #1. 문자로 변환
    #numbers의 모든 요소들을 문자열로 변환.
    #ex) [6,10,2]->['6','10','2']
    #list(map()): 변환된 결과를 다시 리스트로 감싼다
    numbers=list(map(str,numbers))

    #2. 4자리 수로 변경

    #sort(): 원본 자체를 정렬시켜줌
    #sorted(): 원본을 변형시키지 않고 새로운 list를 반환. key 매개변수를 사용해 사용자 정의 기준으로 정렬 가능
    # key=lambda x: (x*4)[:4]: 정렬 기준으로 사용할 값 정의.

    #x*4: 문자열 x를 4번 반복. 서로 다른 길이의 문자열을 비교할 때 앞자리 값을 중점으로 비교하기 위함.
    #(x*4)[:4]: 반복된 문자열에서 앞 4자리만 가져옴.
    #10101010[:4]->1010
    #reverse=True: 내림차순으로 정렬.(큰~작)

    numbers = sorted(numbers, key=lambda x: (x*4)[:4], reverse=True)

    #3. 문자를 합친다. [6,2,10]으로 정렬됐으면 6210
    #0000이면 0 출력. int 변환 후 다시 str로 형변환
    answer=str(int("".join(numbers)))

    return answer