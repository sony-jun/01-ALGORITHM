# 게임 참가자 수
n = int(input())

# 각 게임 회차별 점수를 저장할 리스트
one = []
two = []
three = []

# 참가자의 점수들 입력받아 각 회차에 점수 저장
for _ in range(n) :
    a, b, c = map(int, input().split())
    one.append(a)
    two.append(b)
    three.append(c)

# 회차에 저장된 점수가 중복이 없으면 점수를 더해주기
for i in range(n) :
    score = 0
    if one.count(one[i]) < 2 :
        score += one[i]

    if two.count(two[i]) < 2 :
        score += two[i]

    if three.count(three[i]) < 2 :
        score += three[i]        

    print(score)