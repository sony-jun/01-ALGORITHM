import sys
sys.stdin = open('모음의개수_input.txt')

# 'a', 'e', 'i', 'o', 'u'
while True:
    sentence = input()
    cnt = 0

    if sentence == '#':
            break
    for s in sentence:
        if s in 'aeiouAEIOU':
            cnt += 1
    print(cnt)