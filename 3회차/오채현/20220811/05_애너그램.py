import sys
sys.stdin = open('05_input.txt')

T = int(input())

for _ in range(T):
    w1, w2 = map(str, input().split())
    sw1 = sorted(list(w1))
    sw2 = sorted(list(w2))

    if sw1 == sw2:
        print(f'{w1} & {w2} are anagrams.')
    else:
        print(f'{w1} & {w2} are NOT anagrams.')
