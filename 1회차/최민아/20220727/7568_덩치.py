import sys
sys.stdin = open("20220727/7568_덩치.txt")

people = int(input())
kg_cm = []

for i in range(people):
    weight, height = map(int, input().split())
    kg_cm.append((weight, height))

for i in range(people):
    rank = 1
    for j in range(people):
        if kg_cm[i][0] < kg_cm[j][0] and kg_cm[i][1] < kg_cm[j][1]:
            rank += 1
    print(rank, end=' ')
