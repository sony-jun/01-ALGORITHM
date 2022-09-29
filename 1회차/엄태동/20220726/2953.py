score=0
Winner=0
for i in range(1, 6):
    a,b,c,d = map(int, input().split())
    if score < a+b+c+d:
        score = a+b+c+d
        Winner = i
print(Winner, score, end='')