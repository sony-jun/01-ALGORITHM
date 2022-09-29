#https://www.acmicpc.net/problem/7568
T = int(input())
total = []

for i in range(T):
    w, h = map(int, input().split())
    total.append([w, h]) #각각의 체중, 신장을 받아서 리스트에 저장

rank = []

for j in range(len(total)):
    #각 사람별로 비교하기
    cnt = 1 #기본값 1로 설정
    for n in range(len(total)):
        #
        if total[j][0] < total[n][0] and total[j][1] < total[n][1]:
            cnt += 1 #뒤의 값과 비교했을때 자신보다 큰 값이 있으면 cnt 증가
        #자신보다 큰 값이 없으면 넘어감
    rank.append(cnt)

print(' '.join([str(a) for a in rank]))