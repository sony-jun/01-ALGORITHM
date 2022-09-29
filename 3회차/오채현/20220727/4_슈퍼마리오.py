#https://www.acmicpc.net/problem/2851
#문제)) 버섯의 점수 총합이 100에 가깝게, 비슷한 값이 나오면 그 중 큰 값으로 출력

#점수획득을 중간에 멈추면 끝이기 때문에 for 반복문 사용해서 처음부터 시작해서 중간에 break, 아니면 끝까지 순회

total = 0
result = []

for i in range(10):
    result.append(int(input())) #각각의 버섯들 점수 입력받기

for j in result:
    total += j
    #입력 받은 버섯의 점수 하나씩 더해감
    if total >= 100:
        #점수 총합이 100이상인 경우 - 이렇게하면 100이하의 최대값은 알아서 출력됨(순차적으로 점수를 쌓아나가니까...)
        if total - 100 > 100 - (total - j):
            #현재 점수에서 100뺀 값과 이전 점수에서 100뺀 값을 비교해서 이전 값이 더 작으면 이번에 더한 값을 빼고 이전 값을 total에 넣음(100에 더 가까운 값을 구하기 위해서 하는 것)
            total -= j
        break
print(total)