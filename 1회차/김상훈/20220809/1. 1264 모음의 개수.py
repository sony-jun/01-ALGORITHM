import sys
sys.stdin = open("1. 모음의 개수.txt", "r")

input = sys.stdin.readline


while True:
    word = input()
    if word == '#':
        break
    cnt = 0
    for i in word:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
    