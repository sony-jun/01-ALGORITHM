# 거절당하는 사람의 수를 출력하는 프로그램을 작성하시오.
# 구현

N = int(input())
denied = 0
enter_list = list(map(int,input().split()))
enter = set(enter_list)
for i in enter:
    call=0
    for j in enter_list:
        if i==j:
            call+=1
            if call>=2:
                denied+=1
print(denied)