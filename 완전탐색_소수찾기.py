
def solution(numbers):


    def permutations(current, remaining):
        #현재 조합을 숫자로 만들어 리스트에 추가

        if current:
            all_numbers.add(int(current))

        for i in range(len(remaining)):
            permutations(current+remaining[i],remaining[:i]+remaining[i+1:])

    #소수 판별
    def is_prime(n):
        if n<2:
            return False

        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                return False

        return True

    #모든 가능한 숫자 저장하는 집함
    all_numbers=set() #중복 안 되니까 set으로 넣음

    #재귀 함수로 모든 조합 생성
    permutations("",numbers)

    #소수 개수 계산
    answer=sum(1 for  num in all_numbers if is_prime(num))

    return answer