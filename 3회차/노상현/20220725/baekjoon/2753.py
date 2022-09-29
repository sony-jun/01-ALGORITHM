a = int(input())
# 4로 나눴을때 나머지가 0이고, 100으로 나눴을때 0이 아니면 1을 출력한다.
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)
