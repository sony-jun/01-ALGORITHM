people = int(input())
metrix = [list(map(int, input().split())) for _ in range(people)]
get_point = [0] * people

for i in range(3):
    stripe = []
    for j in range(people):
        stripe.append(metrix[j][i])
    
    for j in range(people):
        if stripe.count(stripe[j]) == 1:
            get_point[j] += stripe[j]

for i in range(people):
    print(get_point[i])