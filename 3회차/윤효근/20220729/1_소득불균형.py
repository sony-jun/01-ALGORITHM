import sys

sys.stdin = open("소득불균형.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    money = list(map(int,input().split()))
    aver = sum(money)//n
    for i in money:
        if i <= aver:
            cnt +=1

    print(f'#{test_case} {cnt}')