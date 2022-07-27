# https://www.acmicpc.net/problem/4673

numbers = list(range(1, 10001))
not_answer = []

for i in numbers:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        not_answer.append(i)
for k in set(not_answer):
    numbers.remove(k)
for answer in numbers:
    print(answer)