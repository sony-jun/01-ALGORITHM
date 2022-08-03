festival_1 = [5000000] + [3000000] * 2 + [2000000] * 3 + [500000] * 4 + [300000] * 5 + [100000] * 6
festival_2 = [5120000] + [2160000] * 2 + [1280000] * 4 + [640000] * 8 + [320000] * 16

n = int(input())

for tc in range(n):
    a, b = map(int, input().split())
    print(festival_1[a-1] + festival_2[b-1])