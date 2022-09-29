# 덩치
# 문제 : 몸무게와 키로 구성된 덩치를 비교하기, 둘다 커야 덩치가 큰 사람

n = int(input())  # 5

student = []  # (wei, hei), (wei, hei), ...

for _ in range(n):
    wei, hei = map(int, input().split())
    student.append((wei, hei))

for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
