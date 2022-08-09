import sys
sys.stdin = open('1526.txt')

N = int(input())

while True:
    cnt = 0
    for i in str(N):
        if i != '4' and i !='7':
            cnt = 1
            N -= 1
    if cnt == 0:
        print(N)
        break