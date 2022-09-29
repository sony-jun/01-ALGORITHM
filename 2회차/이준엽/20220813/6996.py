from hashlib import blake2b

t = int(input())
for i in range(t):
    a, b = input().split()
    b1 = b
    if len(a) == len(b):
        for chr in a:
            if chr in b:
                b=b.replace(chr,'',1)
        if b == '':
            answer = 'anagrams.'
        else:
            answer = 'NOT anagrams.'
    else:
        answer = 'NOT anagrams.'
    print(f'{a} & {b1} are {answer}')
