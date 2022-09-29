# https://www.acmicpc.net/problem/7568

# 덩치
# 몸무게와 키를 받아서
# 둘다크면 덩치가 큰거고
# 하나만 크면 덩치가 같은것
# 중복등수를 인정해준다.

T = int(input())
list_student = []
for i in range(1, T+1):
    x= list(map(int, input().split()))
    list_student.append(x)

for i in list_student:
    rank = 1
    for j in list_student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")