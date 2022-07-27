import sys

sys.stdin = open("input.txt")

# ------- 밑에 입력 --------


n = int(input())

student = []

for _ in range(n):
    wei, hei = map(int, input().split())
    student.append((wei, hei))

for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
