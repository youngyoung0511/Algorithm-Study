def solution(routes):
    # 1. 차량 경로를 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준으로 오름차순 정렬

    # 2. 카메라 설치 개수와 마지막 카메라 설치 위치 초기화
    cameras = 0  # 설치된 카메라 개수
    last_camera = -30001  # 초기값: 카메라가 설치되지 않은 상태

    # 3. 차량 경로 순회
    for start, end in routes:
        # 현재 차량이 기존 카메라 범위를 벗어났다면
        if last_camera < start:
            cameras += 1           # 새로운 카메라 설치
            last_camera = end      # 현재 차량의 진출 지점에 카메라 설치

    # 4. 최소 카메라 개수 반환
    return cameras


#코드 동작 과정
#예제 입력:
#routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

#1. 정렬
#차량 경로를 진출 지점 기준으로 정렬:
#[[-20, -15], [-18, -13], [-14, -5], [-5, -3]]

#2. 순회 및 카메라 설치
#cameras = 0, last_camera = -30001 초기화.
#각 차량 경로를 순회하며 조건을 확인:


#첫 번째 차량: [-20, -15]
#last_camera = -30001, start = -20
#last_camera < start → 새로운 카메라 설치.
#cameras = 1, last_camera = -15.

#두 번째 차량: [-18, -13]
#last_camera = -15, start = -18
#last_camera >= start → 기존 카메라 범위에 포함됨.
#카메라 설치 불필요.

#세 번째 차량: [-14, -5]
#last_camera = -15, start = -14
#last_camera < start → 새로운 카메라 설치.
#cameras = 2, last_camera = -5.

#네 번째 차량: [-5, -3]
# last_camera = -5, start = -5
# last_camera >= start → 기존 카메라 범위에 포함됨.
# 카메라 설치 불필요.

#3. 결과 반환
#최소 카메라 개수: cameras = 2.