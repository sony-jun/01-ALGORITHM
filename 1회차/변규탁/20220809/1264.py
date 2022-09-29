vowel = ["a", "e", "i", "o", "u"]


while True:
    N = input().lower()
    if N == '#':
        break
    count = 0
    for i in vowel:
        if i in N:
            count += N.count(i)
    print(count)