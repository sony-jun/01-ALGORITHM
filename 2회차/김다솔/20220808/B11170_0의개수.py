import sys
sys.stdin = open('B11170.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    zero = 0
    for num in range(N, M+1):
        num_l = list(str(num))
        # print(num_l)
        zero += num_l.count('0')
        
    print(zero)
            