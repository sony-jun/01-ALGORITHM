import sys
sys.stdin = open("30_나는요리사다.txt", "r")



result = []

for i in range(5):
    score = list(map(int, input().split()))
    result.append(sum(score))

print(f"{result.index(max(result))+1} {max(result)}")