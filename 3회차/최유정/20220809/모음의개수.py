# https://www.acmicpc.net/problem/1264

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    str = input()
    cnt = 0
    if str == "#":
        break
    for i in str.lower():
        if i in vowels:
            cnt += 1
    print(cnt)