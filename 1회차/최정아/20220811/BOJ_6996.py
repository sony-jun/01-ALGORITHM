n = int(input())
for _ in range(n):
    a, b = input().split()
    s_a = sorted(a) # sorted 통해서 사전순으로 정렬
    s_b = sorted(b)

    if s_a == s_b: # a와 b 문자열이 같으면 anagrams
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')