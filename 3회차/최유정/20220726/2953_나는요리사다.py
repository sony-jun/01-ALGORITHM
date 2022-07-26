# 점수는 1점부터 5점까지 있다.

# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

sum_list = []

for i in range(5):
    a,b,c,d = map(int, input().split())
    sum_list.append(a+b+c+d)

print(i, max(sum_list))