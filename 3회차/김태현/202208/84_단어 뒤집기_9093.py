import sys
sys.stdin = open("84_단어 뒤집기_9093.txt", "r")

T = int(input())

for _ in range(T):
    words = input().split()
    new = []
    for word in words:
        new.append(word[::-1])
    print(*new)