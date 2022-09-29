# 점수 : 1~5 
t = []

for i in range(5):
    score = list(map(int, input().split()))
    t.append(sum(score))
print(t.index(max(t))+1, max(t))