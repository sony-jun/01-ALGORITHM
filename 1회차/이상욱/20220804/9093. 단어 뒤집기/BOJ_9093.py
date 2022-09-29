import sys
sys.stdin = open ('9093.txt')

T = int(input())

for i in range(1, T+1):
    words = list(input().split())
    for i in range(len(words)):
        print(words[i][::-1], end=' ')
    print()