import heapq

def solution(jobs):
    #1. 요청 시간 순으로 정렬
    jobs.sort(key=lambda x:x[0])

    # 2. 용어 정의
    current_time=0 #현재 시간
    total_time=0 # 총 반환 시간
    completed_jobs=0 # 완료된 작업 수

    wait_queue=[] # 대기 큐

    job_index=0 # jobs 배열의 인덱스

    while completed_jobs < len(jobs):

        #현재 시간까지 요청된 작업을 대기 큐에 삽입
        while job_index<len(jobs) and jobs[job_index][0]<=current_time:
            #대기 큐에 (소요시간, 요청 시간) 형태로 삽입
            heapq.heappush(wait_queue, (jobs[job_index][1],jobs[job_index][0]))
            job_index +=1

            if wait_queue:
                # 대기 큐에서 가장 소요 시간이 짧은 작업 꺼내기
                duration, start_time=heapq.heappop(wait_queue)

                current_time+=duration # 작업 수행
                total_time += current_time-start_time # 반환 시간 계산
                completed_jobs +=1 # 완료된 작업 수 증가

            else:
                # 대기 큐가 비어있으면 다음 작업의 요청 시간으로 이동
                current_time=jobs[job_index][0]

    # 평균 반환 시간 return
    return total_time // len(jobs)

