score = []
sum_score = []
for t in range(10):
    score.append(int(input()))
#print(score) [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 리스트에 숫자 추가

sum_plus = 0
for plus in score:
    sum_plus += plus
    sum_score.append(sum_plus)
#print(sum_score) [1, 3, 6, 11, 19, 32, 53, 87, 142, 231] 누적 합 리스트

x = []
for near in sum_score:
    x.append(abs(100 - near))
#print(x) #[99, 97, 94, 89, 81, 68, 47, 13, 42, 131] 100 - 절대값 리스트
#print(min(x)) 13

for i in range(1, len(x)): 
    if x[i-1] == x[i]:
        print(sum_score[i])
        break
    elif x[i-1] != x[i]:
        print(100-min(x)) #87
        break