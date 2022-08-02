# 1. 문제를 읽고 이해한다
# 테스트 케이스가 주어지고
# 정수 r, e, c를 받는데 
# r은 광고를 하지 않을 때 수익 
# e는 광고를 했을때의 
# 수익 c는 광고비용이다
# 광고하지 않을 때 수익과 광고비용을 합하고 광고를 했을 때의 비용을 구하는 문제다
# 이득일 땐 advertise, 같을 땐 does not matter, 손해일 땐do not advertise로 출력해라


# 2. 문제를 익숙한 용어로 재정의한다
# r = 0
# e = 100
# c = 70

# r + c < e = advertise

# r + c = e = does not matter

# r + c > e = do not advertise
# 3.어떻게 해결할지 계획을 세운다

# 테스트 케이스를 받을 input()을 받고, r c e의 input도 받아준다
# 그 후 if 문으로 비교 해주면 될것 같다

# 4. 프로그램으로 구현한다
t = int(input())

for i in range(1,t+1):
    r, e, c = map(int,input().split())
    sum_ = r + c
    if sum_ < e:
        print('advertise')
    elif sum_ == e:
        print('does not matter')
    else:
        print("do not advertise")


# 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다
# r e c를 받아주고 r+e 비교 c니까 공통적으로 쓰는 r+e를 sum_이란 변수로 담아주고
# sum_과 c를 비교해 프린트문으로 출력했다 
