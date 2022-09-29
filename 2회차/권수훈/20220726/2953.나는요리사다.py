# "나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다.
# 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.

# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.
sum_value = []

for _ in range(5) :
  sum_value.append(sum(map(int, input().split())))

print(sum_value.index(max(sum_value))+1, max(sum_value))
