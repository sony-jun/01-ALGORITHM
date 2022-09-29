score_list = []
score = 0

for i in range(10):
    score_list.append(int(input()))

for i in score_list:
    score += i
    if score >= 100:
        prev_score = score - i 
        out = prev_score if score - 100 >= 100 - prev_score else score
        break      
print(out) 