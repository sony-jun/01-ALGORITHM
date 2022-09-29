import sys
sys.stdin = open("2_자료구조는 정말 최고야.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
answer = True
for i in range(M):
    bookcount = int(input())
    bookstack = list(map(int, input().split()))

    for k in range(bookcount-1):
        if bookstack[k] < bookstack[k+1]:
            answer = False

if answer:
    print('Yes')
else:
    print('No')