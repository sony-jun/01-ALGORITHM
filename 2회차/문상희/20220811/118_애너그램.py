test = int(input())

for _ in range(test):
    a, b = list(map(str, input().split()))
    anagram = 1
    if set(a) != set(b) or len(a) != len(b):
        anagram = 0
    check = list(set(a))
    for i in check:
        if a.count(i) != b.count(i):
            anagram = 0

    if anagram == 1:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')