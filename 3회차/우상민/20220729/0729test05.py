# 신용카드 만들기 1

#신용카드 번호는 룬 공식(LUHN Formula)을 만족해야합니다.
# 룬 공식이란 카드 번호에서 마지막 자리(열여섯번째) 숫자N을 구하는 공식입니다.

# 1) 매 홀수자리의 숫자마다 2를 곱해서 더합니다. 
# 2) 매 짝수자리의 숫자는 그대로 더합니다.
# 3) 1)과 2)를 더 한 숫자에 N을 더 한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효한 숫자입니다. 

# 16자리의 카드 번호 중 처음 15개가 주어졌을 때 룬 공식을 만족하기 위해 마지막에 들어가야하는 숫자N을 구하는 프로그램을 작성하시오.

# EX) 4520 0200 1900 416N
# 1) 홀수 자리 수 (4 x 2) + (2 x 2) + (0 x 2) + (0 x 2) + (1 x 2) + (0 x 2) + (4 x 2) + (6 x 2)
# 2) 짝수 자리 수 5 + 0 + 2 + 0 + 9 + 0 + 1 
# 3) N을 제외한 1) 과 2)를 더한 합은 51이므로 N의 값은 9입니다.
 
T = int(input())
for i in range(1, T+1):
    N = input().split()
    count = 0
    for idx in range(0, 15):
        if (idx+1) % 2 == 0:
            count += int(N[idx])
        elif (idx+1) % 2 == 1:
            count += int(N[idx])*2
    if count % 10 == 0:
        print(f'#{i}', 0)
    elif count % 10 == 1:
        print(f'#{i}', 9)
    elif count % 10 == 2:
        print(f'#{i}', 8)
    elif count % 10 == 3:
        print(f'#{i}', 7)
    elif count % 10 == 4:
        print(f'#{i}', 6)
    elif count % 10 == 5:
        print(f'#{i}', 5)
    elif count % 10 == 6:
        print(f'#{i}', 4)
    elif count % 10 == 7:
        print(f'#{i}', 3)
    elif count % 10 == 8:
        print(f'#{i}', 2)
    elif count % 10 == 9:
        print(f'#{i}', 1)
