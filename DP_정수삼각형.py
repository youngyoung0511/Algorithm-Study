
def solution(triangle):
    #triangle의 길이가 1이면 바로 return
    if len(triangle)==1:
        return triangle[0][0]
    
    #아래서부터 위로 합을 계산
    for row in range(len(triangle) -2,-1,-1): #삼각형의 아래부터 위로 이동 #len(triangle): 전체 높이 #len(triangle)-2: 아래에서 두번째 줄 인덱스 #-1은 인덱스 0까지 포함하도록 #-1은 반복이 아래에서 위로 진행되도록
        for col in range(len(triangle[row])):
            
            #아래 두개 중에 큰 값을 더함
            triangle[row][col]+=max(triangle[row+1][col],triangle[row+1][col+1])
            # triangle[row + 1][col]: 현재 위치 바로 아래(왼쪽 대각선)의 숫자
            # triangle[row + 1][col + 1]: 현재 위치 바로 아래(오른쪽 대각선)의 숫자
            
    # 최종적으로 triangle[0][0]에 최댓값 저장
    return triangle[0][0]