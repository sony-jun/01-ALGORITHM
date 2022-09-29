# 2711
import sys
sys.stdin = open("창영.txt")

for _ in range(int(input())):
    N, words = input().split()
    answer = ''
    for idx in range(len(words)):
        if idx == int(N) -1:
            continue
        answer += words[idx]
    print(answer)