#array, command가 들어와
def solution(array, commands):
    answer=[] #결과값 저장

    # 명령어 리스트의 길이 계산.
    #command는 [i, j, k] 형태로 주어지기 때문
    length=len(commands)

    for i in range(length): #i: 명령어의 인덱스
        #[0]: 자르기 시작하는 위치
        #[1]: 끝 위치
        #[2]: k번째

        #-1해서 슬라이싱 시작 위치 맞춰줌. (파이썬은 0부터 시작이라)
        new_array=array[commands[i][0]-1: commands[i][1]]#i부터 j까지 잘라서 새로운 arrary 생성
        new_array.sort() #정렬

        answer.append(new_array[commands[i][2]-1])#K번째 수 결과 리스트에 넣기

    return answer