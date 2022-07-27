a = int(input())
list = []
for i in range(a):
    list.append(input().split())
for i in range(a):
    grade = 1
    for j in range(a):
        if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
            grade = grade +1
    print(grade, end=' ')