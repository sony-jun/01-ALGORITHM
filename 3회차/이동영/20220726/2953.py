T = 5

total_score_list = {}

for i in range(1,T+1):
    score_list = list(map(int,input().split()))
    total_score_list[i] = sum(score_list)
max_key = max(total_score_list, key = total_score_list.get)

print(max_key, total_score_list.get(max_key))