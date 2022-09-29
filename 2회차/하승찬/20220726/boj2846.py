# 상근이는 자전거를 타고 등교한다. 자전거 길은 오르막길, 내리막길, 평지로 이루어져 있다
# . 상근이는 개강 첫 날 자전거를 타고 가면서 일정 거리마다 높이를 측정했다.
#  상근이는 가장 큰 오르막길의 크기를 구하려고 한다.

# 측정한 높이는 길이가 N인 수열로 나타낼 수 있다. 여기서 오르막길은 적어도 2개의 수로 이루어진 높이가
#  증가하는 부분 수열이다. 오르막길의 크기는 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이이다.

# 예를 들어, 높이가 다음과 같은 길이 있다고 하자.
#  12 3 5 7 10 6 1 11. 이 길에는 2 개의 오르막길이 있다.
#  밑 줄로 표시된 부분 수열이 오르막길이다. 첫 번째 오르막길의 크기는 7이고,
# 두 번째 오르막길의 크기는 10이다. 높이가 12와 6인 곳은 오르막길에 속하지 않는다.



# 가장 큰 오르막길을 구하는 프로그램을 작성하시오.
len_num=int(input())
n= list (map(int,input().split()))

high=[]
max_count=0
cnt= n[0]
for nums in range(0,len_num) :
    if n[nums] > cnt:
        max_count += n[nums]-cnt
        cnt = n[nums]
    elif n[nums]<= cnt:
        high.append(max_count)
        cnt = n[nums]
        max_count = 0
    # elif n[nums]== cnt:
    #     cnt = n[nums]
high.append(max_count)
    # if cnt ==len_num-1:
    #     break

print(max(high))

#처음높이랑... 내리막에서 내려간 길이는 포함을 안한대요..**연달아 오르는 숫자만 계산을해야하나봐요..

# len_num=int(input())
# n= list (map(int,input().split()))

# high=[]
# max_h=n[0]
# min_h=n[0]
# cnt= n[0]
# for nums in range(0,len_num) :
#     if 