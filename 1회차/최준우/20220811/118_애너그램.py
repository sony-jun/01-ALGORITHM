# https://www.acmicpc.net/problem/6996

T = int(input())

for _ in range(T):
    alphabet = [0] * 26
    a, b = input().split()

    for i in range(len(a)):
        alphabet[ord(a[i])-97] += 1
    for i in range(len(b)):
        alphabet[ord(b[i])-97] += 1
    
    for i in range(len(alphabet)):
        if alphabet[i] % 2 != 0:
            print(f'{a} & {b} are NOT anagrams.')
            break
    else:
        print(f'{a} & {b} are anagrams.')