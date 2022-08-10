import sys

input = sys.stdin.readline
n = int(input())
numbers = []
#숫자들을 받아 numbers(list)에 append하기
for i in range(n):
    numbers.append(list(map(int,input().split(' '))))


scoreList = []
for j in range(n):
    for i in range(n-1):
        if numbers[i][j] == numbers[i+1][j]:
            continue
        else :
            score = numbers[]

    print('--------')


