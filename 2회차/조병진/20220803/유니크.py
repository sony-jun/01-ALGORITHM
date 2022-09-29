# 유니크
# 문제 : 자신과 같은 수를 쓴 사람이 없으면 점수를 얻고, 겹치면 점수를 얻을 수 없다.
#       3번의 게임에서 얻은 총 점수 구하기

n = int(input())

one = []  # 게임 점수 리스트
two = []
three = []

for _ in range(n):
    a, b, c = map(int, input().split())
    one.append(a)
    two.append(b)
    three.append(c)

for i in range(n):
    total = 0
    if one.count(one[i]) == 1:  # 게임 점수 리스트에서 i 요소가 1개 있는지 확인
        total += one[i]  # 해당 점수 더하기
    if two.count(two[i]) == 1:
        total += two[i]
    if three.count(three[i]) == 1:
        total += three[i]

    print(total)
