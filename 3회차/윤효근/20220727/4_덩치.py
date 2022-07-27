import sys

sys.stdin = open("4_덩치.txt")

number = int(input())
w_list = []
rank = 1

for i in range(0, number):
    a = map(int, input().split())
    w_list.append(list(a))

for i in range(len(w_list)):
    for j in range(len(w_list)):
        if w_list[i][0] < w_list[j][0] and w_list[i][1] < w_list[j][1]:  # 각각의 무게와 키를 비교
            rank += 1  # 둘다 작을경우 등수 증가

    print(rank, end=' ')  # 등수를 출력
    rank = 1  # 등수를 초기화