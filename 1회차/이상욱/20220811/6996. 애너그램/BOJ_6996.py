import sys
sys.stdin = open('6996.txt')

T = int(input())

for _ in range(T):
    a, b = map(str, input().split())
    A = sorted(list(a))
    B = sorted(list(b))
    if A == B:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')