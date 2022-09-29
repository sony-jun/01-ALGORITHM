import sys
sys.stdin = open('6996.txt')

T = int(input())

for _ in range(T):
    A, B = input().split()

    list_A = sorted(list(A))
    list_B = sorted(list(B))
    print(list_A)

    if list_A == list_B:
        print(A + '&' + B + 'are anagrams.')
    else:
        print(A + '&' + B + 'are NOT anagrams.')
