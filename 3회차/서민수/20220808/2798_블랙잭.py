# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 


# 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 
# 그런 후에 딜러는 숫자 M을 크게 외친다.

# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때,
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# M == 21 M >= 21

# 카드 갯수와 카드 점수
N, M = map(int, input().split())

# 각 카드의 숫자
CARD_ = list(map(int,input().split()))
# 결과값
result = 0
# 3개의 값을 받기 위해 3중 for문
for i in range(N):
    # 2번째 카드
    for j in range(i+1, N):
        # 3번째 카드
        for k in range(j+1, N):
            # M보다 작거나 같으면 
            if CARD_[i] + CARD_[j] + CARD_[k] <=M:
                # reuslt에 담아주기 단 3개 중 큰걸로 max함수 쓰기
                result = max(result, CARD_[i] + CARD_[j] + CARD_[k])
print(result)