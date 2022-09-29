import sys
sys.stdin = open('1264.txt')

case = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    word = input()
    cnt = 0
    if word == '#':
        break
    for i in range(len(word)):
        if word[i] in case :
            cnt += 1
    print(cnt)
