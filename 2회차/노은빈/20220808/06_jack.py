import sys
input = sys.stdin.readline

n, m = map(int,input().split())  #카드의 개수 n,m
cards = list(map(int,input().split()))  #카드에 쓰여 있는 수
total = 0 #m을 넘지 않으면서 m에 가까운 카드 수

for i in range(n): #n만큼 반복
    #인덱스 0, 1, 2
    for j in range(i+1, n): #중복된 카드를 없애기 위해서(외우지 말고 손으로써보기)
    #인덱스 1, 2, 3
        for k in range(j+1, n):
        #인덱스 2, 3, 4
            if cards[i] + cards[j] + cards[k] > m : #중복되지 않는 각각의 카드의 수의 합이 m보다 크면
                continue

            else: #m보다 작다면 
                total = max(total, cards[i]+cards[j]+cards[k]) #작은 수들 중 가장 큰 값을 출력
print(total)  