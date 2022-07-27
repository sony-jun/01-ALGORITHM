# 2851번 슈퍼 마리오

score = 0
score_dict = {}
a = 0
b = 0

for i in range(1, 11):
    s = int(input())
    score += s
    score_dict[i] = score

for j in range(1, len(score_dict)) :
    if score_dict[j] >= 100:
        a = score_dict[j]
        b = score_dict[j-1]
        break

if abs(a - 100) != 0:
    if abs(a - 100) <= abs(b - 100):
        print(a)
    elif abs(a - 100) > abs(b - 100):
        print(b)
else:
    print(a)
