import sys

sys.stdin = open("신용카드 만들기 1.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    n = list(map(int,input().split()))
    for i in range(len(n)):
        if i %2 == 0:     #홀수자리 *2지만 인덱스는 0부터 시작이므로 홀수자리 == 인덱스의 짝수자리 이다
            n[i] *= 2     #홀수자리에만 *2를 하고 짝수자리는 그대로이다
    N = 10-(sum(n)%10)
    #N은 모든숫자의 합을 10으로 나눠떨어지게하는 숫자이므로 (N을 제외한 모든 숫자의 합을 10으로 나눈 나머지) -10이다
    if N ==10:  #모든숫자가 10으로 나눠떨어질경우 N은 0이지만 10으로 출력되기때문에 0으로 바꿔준다
        N=0
    print(f'#{test_case} {N}')
