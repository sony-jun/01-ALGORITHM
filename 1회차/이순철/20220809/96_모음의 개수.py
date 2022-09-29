# https://www.acmicpc.net/problem/1264

import sys
sys.stdin = open('_모음의 개수.txt')

cnt = 0
while True:
    word = input().lower()
    if "#" in word:
        break
    for i in word:
        if i in 'aeiou':
            cnt += 1
    print(cnt)
    cnt = 0
