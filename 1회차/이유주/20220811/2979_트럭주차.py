import sys
sys.stdin = open("input.txt")
#주차요금 얼마내야하는지 계산하는 프로그램
#에제2
# 10 8 6  : 1~3대당 주차 요금
# 15 30   : 트럭 1 이 도착한 시간과 떠난 시간
# 25 50
# 70 80
one_fee, two_fee, three_fee = map(int,input().split()) #주차된 차 수 당 주차요금 입력

time= [list(map(int,input().split())) for _ in range(3)]# 트럭당 도착시간, 떠난시간 입력. 트럭이 세대이기 때문에 그만큼 반복
maxtime = max(time[x][1] for x in range(3)) # 
parking = [0] * (100)
#이 경우 떠난 시간 중 가장 큰 시간은 80분이다. 그래서 각 분마다 주차된 차수를 입력하기 위해서 요소의 개수 마련해야하는데 parking의 인덱스는 0~ 80이므로 81개를 곱한다.

#트럭 한대씩 도착시간,떠난시간 나열
for t in time:
    #예)t = [15, 30] = time[0] 트럭1이 주차한 시간
    for i in range(t[0]+1, t[1]+1):# 30-15하면 15가나와야하므로
        parking[i] += 1 # 인덱스 15~30에 값으로 각각 1씩 추가. 트럭이 한대 주차되었다는 의미.이경우 인덱스가 시간(분)이고 값이 트럭수다.
        

fee = 0 #출력할 최종요금
for truck in parking:
    print(truck.index)
    # 0분에서 80분까지 트럭의 주차된 수. 총 81번 반복된다.
    if truck == 1: #주차된 차가 하나라면
        fee += one_fee * 3 #1대가 주차한 시간(분)에 * 1대의 요금이지만 15분에 10원, 16분에 10원 이런식으로 처리해야하기때문에 + 사용.
    elif truck == 2:
        fee += two_fee * 2  #주차된 차 수를 곱해주기
    elif truck == 3: #else를 사용할수 없는이유는 값이 0인곳도 있기 때문.
        fee += three_fee * 3

# print(fee)