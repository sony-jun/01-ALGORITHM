import sys

sys.stdin = open("신용카드 만들기 2.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n= list(map(str,input()))

    if (n[0] == '3' or n[0] == '4' or n[0] == '5' or n[0] == '6' or n[0] == '9') and len(n) - n.count('-') == 16: #3 4 5 6 9로 시작하지 않으면 0출력
         print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')