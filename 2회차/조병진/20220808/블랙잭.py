# 블랙잭 🐳
# 문제 : 합이 M을 넘지 않으면서 최대한 가까운 카드 3장 구하기

N, M = map(int, input().split())

cards = list(map(int, input().split()))  # [5, 6, 7, 8, 9]

answer = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]  # 해당 인덱스의 값 더하기

            if answer < total <= M:  # M은 넘지 않은 수로 값을 리셋
                answer = total
            if total == M:
                answer = total

print(answer)
