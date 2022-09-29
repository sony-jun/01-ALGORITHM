# 11170번 0의 개수

# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.
# 예를 들어, N, M이 각각 0, 10일 때 0을 세면 0에 하나, 10에 하나가 있으므로 답은 2이다.


# 출력
# 각각의 테스트 케이스마다 N부터 M까지의 0의 개수를 출력한다.


import sys

# 첫째 줄에 테스트 케이스의 개수가 주어진다.
T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, input().split())
    count = 0
    
    for n in range(N, M+1):
        # print(list(str(n)))
        if '0' in list(str(n)):
            count += list(str(n)).count('0')

    print(count)