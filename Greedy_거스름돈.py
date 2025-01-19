n=1260
count=0

#화페 리스트
array=[500,100,50,10]

#동전을 확인 하면서
#count(결과값)에 coin을 나눈 몫을 담음
for coin in array:
    count+=n//coin
    n%=coin


print(count)
# 1121