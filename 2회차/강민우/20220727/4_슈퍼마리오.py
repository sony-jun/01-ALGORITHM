score =[]
total =0
new_score ={}
result =[]

for a in range(10) :
    score.append(int(input()))

for a in score :
    total += a
    new_score[total] = abs(total-100)

for a in new_score :
    if new_score[a] == min(new_score.values()) :
        result.append(a)
print(max(result))
        



