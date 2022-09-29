score = []
for t in range(10):
    score.append(int(input()))
#print(score) [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 리스트에 숫자 추가

sum = 0
min = 10e9
max_score = 0
for i in range(10):
    sum += score[i]
    diff = abs(100-sum)
    if diff <= min:
        min = diff
        max_score = sum

print(max_score)