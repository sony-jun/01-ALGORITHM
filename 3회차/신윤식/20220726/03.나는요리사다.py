# 참가자수 5명 / 점수 1~5점

people = 5
score_dict = {}

for i in range(people):
    score = map(int,input().split())
    score_dict[i+1] = sum(score)

Num_Score = sorted(score_dict.items(), key = lambda x:x[1], reverse=True)

print(Num_Score[0][0], Num_Score[0][1])


# 더 좋은 풀이 

num = sum(map(int, input().split()))
winner = 1

for i in range(2, 6):
    temp = sum(map(int, input().split()))

    if num < temp:
        winner = i
        num = temp

print(winner, num)